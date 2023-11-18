import json
import os
import re
from typing import List, Optional

from bs4 import BeautifulSoup

import vonatinfo_client
from vonatinfo_client import StationRequest, Train, TrainScheduleRequest, TrainsRequest

with open(os.path.join(os.path.dirname(__file__), "stations.json")) as stations:
    STATIONS = json.load(stations)


class Vonatinfo:
    async def __aenter__(self):
        self.api_client = vonatinfo_client.ApiClient()
        self.api_instance = vonatinfo_client.DefaultApi(self.api_client)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.api_client.close()

    async def get_trains(self) -> List[Train]:
        request = vonatinfo_client.GetDataPostRequest(
            TrainsRequest(a="TRAINS", jo={"history": False, "id": False})
        )

        response = await self.api_instance.get_data_post(request)

        return response.actual_instance.d.result.trains.train

    async def get_station(self, station_name: str):
        request = vonatinfo_client.GetDataPostRequest(
            StationRequest(a="STATION", jo={"a": station_name})
        )

        response = await self.api_instance.get_data_post(request)

        return parse_station_html(response.actual_instance.d.result)

    async def get_train(self, train_id: str, date: Optional[str] = None):
        param = {"v": train_id}
        if date:
            param["d"] = date

        request = vonatinfo_client.GetDataPostRequest(
            TrainScheduleRequest(a="TRAIN", jo=param)
        )

        response = await self.api_instance.get_data_post(request)

        return parse_train_schedule_html(response.actual_instance.d.result.html)


def parse_station_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    for row in soup.find_all('tr'):
        if row.find_next('th'):
            # Skip header rows
            continue

        columns = row.find_all("td")
        if len(columns) == 1:
            # Detail row, skip for now
            continue
        else:
            # Extract train id from something like this:
            # map.getData('TRAIN', { v: '6447606_231026', d: '23.10.26', language: '1' } )
            train_id_match = re.search(r"v\s*:\s*[\"']([^\"']+)[\"']", row["onclick"])
            if train_id_match:
                train_id = train_id_match.group(1)
            else:
                train_id = None

            (arrival_cell, departure_cell, platform_cell, train_cell) = columns

            arrival_parts = list(arrival_cell.stripped_strings)
            scheduled_arrival = arrival_parts[0] if len(arrival_parts) > 0 else None
            actual_arrival = arrival_parts[1] if len(arrival_parts) > 1 else None

            departure_parts = list(departure_cell.stripped_strings)
            scheduled_departure = departure_parts[0] if len(departure_parts) > 0 else None
            actual_departure = departure_parts[1] if len(departure_parts) > 1 else None

            train_parts = list(train_cell.stripped_strings)
            if len(train_parts) == 3:
                (train_number, train_type, train_relation) = train_parts
                # Replace multiple space and newline with one
                train_type = ' '.join(train_type.split())
            else:
                (train_number, train_relation) = train_parts
                train_type = None

            yield {
                "scheduled_arrival": scheduled_arrival,
                "actual_arrival": actual_arrival,
                "scheduled_departure": scheduled_departure,
                "actual_departure": actual_departure,
                "platform": platform_cell.string,
                "train_number": train_number,
                "train_type": train_type,
                "train_relation": train_relation,
                "train_id": train_id
            }


def parse_train_schedule_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    for row in soup.find_all('tr'):
        if row.find_next('th'):
            # Skip header rows
            continue

        columns = row.find_all("td")
        if len(columns) == 1:
            # Detail row, skip for now
            continue
        else:
            (distance_cell, station_cell, arrival_cell, departure_cell, platform_cell) = columns

            distance = distance_cell.string
            station = "".join(station_cell.stripped_strings)

            arrival_parts = list(arrival_cell.stripped_strings)
            scheduled_arrival = arrival_parts[0] if len(arrival_parts) > 0 else None
            actual_arrival = arrival_parts[1] if len(arrival_parts) > 1 else None

            departure_parts = list(departure_cell.stripped_strings)
            scheduled_departure = departure_parts[0] if len(departure_parts) > 0 else None
            actual_departure = departure_parts[1] if len(departure_parts) > 1 else None

            platform = platform_cell.string
            yield {
                "distance": distance,
                "station": station,
                "scheduled_arrival": scheduled_arrival,
                "actual_arrival": actual_arrival,
                "scheduled_departure": scheduled_departure,
                "actual_departure": actual_departure,
                "platform": platform,
            }
