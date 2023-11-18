import asyncio
from typing import Optional

import fire
from tabulate import tabulate

import vonatinfo_api


async def get_trains():
    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        trains = await vonatinfo.get_trains()
        print(tabulate((train.to_dict() for train in trains), headers={
            "@Delay": "Delay",
            "@Relation": "Relation",
            "@TrainNumber": "Train #",
            "@Line": "Line",
            "@Menetvonal": "Operator",
            "@Lat": "Lat.",
            "@Lon": "Lon.",
            "@ElviraID": "Train ID"
        }))


async def get_station(station_name: str):
    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        station = await vonatinfo.get_station(station_name)
        print(tabulate(station, headers={
            "scheduled_arrival": "Arr.",
            "actual_arrival": "(act.)",
            "scheduled_departure": "Dep.",
            "actual_departure": "(act.)",
            "platform": "Pl.",
            "train_number": "Train #",
            "train_type": "Type",
            "train_relation": "Relation",
            "train_id": "Train ID",
        }))


async def get_train_schedule(train_id: str, date: Optional[str] = None):
    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        train_schedule = await vonatinfo.get_train(train_id, date)
        # print(train_schedule)
        print(tabulate(train_schedule, headers="keys"))


class VonatinfoCli(object):
    def trains(self):
        asyncio.run(get_trains())

    def station(self, station_name: str):
        asyncio.run(get_station(station_name))

    def train_schedule(self, train_id: str, date: Optional[str] = None):
        asyncio.run(get_train_schedule(train_id, date))


if __name__ == '__main__':
    fire.Fire(VonatinfoCli)
