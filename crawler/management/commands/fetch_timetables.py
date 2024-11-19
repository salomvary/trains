import asyncio
import itertools
from datetime import datetime, timezone, timedelta

from django.core.management import BaseCommand

import elvira_api
from crawler.models import Schedule
from elvira_client import Scheduler, Station


class Command(BaseCommand):
    help = "Fetches and persists timetables"

    def add_arguments(self, parser):
        parser.add_argument("--station-codes", nargs="+", type=str)

    def handle(self, *args, **options):
        asyncio.run(fetch_timetables(options["station_codes"]))


async def fetch_timetables(station_codes: list[str]):
    travel_date = datetime.now(timezone.utc) - timedelta(days=1)
    async with elvira_api.Elvira() as elvira:
        for station_code in station_codes:
            await fetch_timetable(elvira, station_code, travel_date=travel_date)


async def fetch_timetable(elvira, station_code: str, travel_date: datetime):
    timetable = await elvira.get_timetable(station_code, travel_date=travel_date)

    await Schedule.objects.abulk_create(
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
    )
