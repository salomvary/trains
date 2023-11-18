from django.http import HttpRequest
from django.shortcuts import render
from django.utils.translation import gettext as _

import vonatinfo_api

TRAINS_HEADERS = {
    "delay": _("Delay"),
    "relation": _("Relation"),
    "train_number": _("Train #"),
    "line": _("Line"),
    "menetvonal": _("Operator"),
    "lat": _("Lat."),
    "lon": _("Lon."),
    "elvira_id": _("Train ID")
}

STATION_HEADERS = {
    "scheduled_arrival": _("Arr."),
    "actual_arrival": _("(act.)"),
    "scheduled_departure": _("Dep."),
    "actual_departure": _("(act.)"),
    "platform": _("Pl."),
    "train_number": _("Train #"),
    "train_type": _("Type"),
    "train_relation": _("Relation"),
    "train_id": _("Train ID"),
}

TRAIN_SCHEDULE_HEADERS = {
    "distance": _("Distance"),
    "station": _("Station"),
    "scheduled_arrival": _("Arr."),
    "actual_arrival": _("(act.)"),
    "scheduled_departure": _("Dep."),
    "actual_departure": _("(act.)"),
    "platform": _("Platform"),
}


async def train_list(request: HttpRequest):
    headers = TRAINS_HEADERS.values()

    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        trains = [
            [getattr(train, key) for key in TRAINS_HEADERS.keys()]
            for train in await vonatinfo.get_trains()]

        return render(request, "trains.html", {"headers": headers, "trains": trains})


async def station_list(request: HttpRequest):
    return render(request, "stations.html", {"stations": vonatinfo_api.STATIONS})


async def station_detail(request: HttpRequest, station_name: str):
    headers = STATION_HEADERS.values()

    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        trains = [
            [train.get(key) for key in STATION_HEADERS.keys()]
            for train in await vonatinfo.get_station(station_name)]
        return render(request, "station_detail.html", {"headers": headers, "trains": trains})


async def train_detail(request: HttpRequest, train_id: str):
    headers = TRAIN_SCHEDULE_HEADERS.values()

    async with vonatinfo_api.Vonatinfo() as vonatinfo:
        train_schedule = [
            [stop.get(key) for key in TRAIN_SCHEDULE_HEADERS.keys()]
            for stop in await vonatinfo.get_train(train_id)
        ]

    return render(request, "train_detail.html", {"headers": headers, "train_schedule": train_schedule})
