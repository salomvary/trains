import asyncio
import itertools
import logging
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

from django.core.management import BaseCommand

import elvira_api
from crawler.models import Schedule
from elvira_client import Scheduler, Station

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Fetches and persists timetables"

    def add_arguments(self, parser):
        parser.add_argument("--station-codes", nargs="+", type=str, default=[])

    def handle(self, *args, **options):
        if not options["station_codes"]:
            logger.error("No station codes provided")
            exit(1)

        asyncio.run(fetch_timetables(options["station_codes"]))


async def fetch_timetables(station_codes: list[str]):
    start_of_today = datetime.now(ZoneInfo("Europe/Budapest")).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    async with elvira_api.Elvira() as elvira:
        # Because we do not yet know how far can delays be updated
        # back in the past anf forward in the future, we will fetch plenty
        # of schedules in the past and future. Ideally, a +/-24 hours
        # window should be a good start.
        # But. ELVIRA API has a peculiar way of getting schedules for certain
        # time frames: the travel date parameter does allow specifying a date and
        # time after which to fetch the schedules, but the end if this time frame
        # can not be specified. It is always the end of the day of the travel date
        # in Europe/Budapest timezone.
        # In order to get a roughly +/-24 hours window, we will fetch schedules
        # for the whole current day, the whole previous day and the whole next day.
        # We could be more clever, and fetch schedules for previous day starting
        # 24 hours ago, but that's all we can optimize, there is no way to save us
        # from fetching schedules for three days.
        # We could also filter what we persist, i.e. discard schedules that are
        # older than 24 hours and further than 24 hours in the future.

        for day_offset in [-1, 0, 1]:
            travel_date = start_of_today + timedelta(days=day_offset)
            for station_code in station_codes:
                logger.info("Fetching timetables for %s", travel_date)
                schedules = await fetch_timetable(
                    elvira, station_code, travel_date=travel_date
                )
                schedules_count = len(schedules)
                if schedules_count > 0:
                    logger.info(
                        "Fetched %s schedules for station %s",
                        schedules_count,
                        station_code,
                    )
                else:
                    logger.error("No schedules fetched for station %s", station_code)


async def fetch_timetable(elvira, station_code: str, travel_date: datetime):
    timetable = await elvira.get_timetable(station_code, travel_date=travel_date)

    return await Schedule.objects.abulk_create(
        itertools.chain(
            (
                map_schedule(Schedule.ScheduleType.ARRIVAL, timetable.station, schedule)
                for schedule in timetable.arrival_scheduler
            ),
            (
                map_schedule(
                    Schedule.ScheduleType.DEPARTURE, timetable.station, schedule
                )
                for schedule in timetable.departure_scheduler
            ),
        )
    )


def map_schedule(
    schedule_type: Schedule.ScheduleType, station: Station, schedule: Scheduler
) -> Schedule:
    return Schedule(
        type=schedule_type,
        # Where
        station_name=station.name,
        station_code=station.code,
        # When
        scheduled_arrival=schedule.arrive,
        scheduled_departure=schedule.start,
        actual_or_estimated_arrival=schedule.actual_or_estimated_arrive,
        actual_or_estimated_departure=schedule.actual_or_estimated_start,
        # What
        train_name=schedule.name,
        train_number=schedule.code,
        train_id=schedule.train_id,
        relation_symbol=(
            schedule.viszonylati_jel.jel if schedule.viszonylati_jel else None
        ),
        kind_name=schedule.kind.name,
        # Start station
        start_station_name=schedule.start_station.name,
        start_station_code=schedule.start_station.code,
        start_station_id=schedule.start_station.id,
        # End station
        end_station_name=schedule.end_station.name,
        end_station_code=schedule.end_station.code,
        end_station_id=schedule.end_station.id,
    )
