import asyncio
from datetime import datetime
from operator import attrgetter

from tabulate import tabulate

import elvira_api
from elvira_client import Scheduler


# logging.basicConfig(level=logging.DEBUG)


def get_train_type(scheduler: Scheduler):
    if scheduler.viszonylati_jel and scheduler.viszonylati_jel.jel:
        return scheduler.viszonylati_jel.jel
    else:
        return scheduler.full_short_type


def get_relation(scheduler: Scheduler):
    return f"{scheduler.start_station.name} - {scheduler.end_station.name}"


ARRIVAL_TIMETABLE_COLUMNS = (
    ("Time", attrgetter("arrive")),
    ("(act.)", attrgetter("actual_or_estimated_arrive")),
    ("Pl.", attrgetter("end_track")),
    ("Train #", attrgetter("code")),
    ("Type", get_train_type),
    ("Relation", get_relation),
    ("Train ID", attrgetter("train_id")),
)

ARRIVAL_TIMETABLE_HEADERS = [header for header, _ in ARRIVAL_TIMETABLE_COLUMNS]


DEPARTURE_TIMETABLE_COLUMNS = (
    ("Time", attrgetter("start")),
    ("(act.)", attrgetter("actual_or_estimated_start")),
    ("Pl.", attrgetter("start_track")),
    ("Train #", attrgetter("code")),
    ("Type", get_train_type),
    ("Relation", get_relation),
    ("Train ID", attrgetter("train_id")),
)

DEPARTURE_TIMETABLE_HEADERS = [header for header, _ in ARRIVAL_TIMETABLE_COLUMNS]


STATIONS_COLUMNS = (
    ("Name", attrgetter("name")),
    ("Station code", attrgetter("code")),
    ("Station ID", attrgetter("id")),
)

STATIONS_HEADERS = [header for header, _ in STATIONS_COLUMNS]


async def get_stations():
    async with elvira_api.Elvira() as elvira:
        stations = await elvira.get_station_list()

        print(
            tabulate(
                (to_row(station, STATIONS_COLUMNS) for station in stations),
                headers=STATIONS_HEADERS,
            )
        )


async def get_timetable(station_number_code: str, travel_date: str = None):
    kwargs = {}
    if travel_date is not None:
        kwargs["travel_date"] = datetime.fromisoformat(travel_date)

    async with elvira_api.Elvira() as elvira:
        timetable = await elvira.get_timetable(station_number_code, **kwargs)

        print("Arrivals")

        print(
            tabulate(
                (
                    to_row(scheduler, ARRIVAL_TIMETABLE_COLUMNS)
                    for scheduler in timetable.arrival_scheduler
                ),
                headers=ARRIVAL_TIMETABLE_HEADERS,
            )
        )

        print("Departures")

        print(
            tabulate(
                (
                    to_row(scheduler, DEPARTURE_TIMETABLE_COLUMNS)
                    for scheduler in timetable.departure_scheduler
                ),
                headers=DEPARTURE_TIMETABLE_HEADERS,
            )
        )


class ElviraCli(object):
    def stations(self):
        asyncio.run(get_stations())

    def timetable(self, station_number_code: str, travel_date: str = None):
        asyncio.run(get_timetable(station_number_code, travel_date))


def to_row(model, columns):
    return [column_getter(model) for _, column_getter in columns]
