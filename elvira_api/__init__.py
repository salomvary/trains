from datetime import datetime, timezone

import elvira_client
from elvira_client import TimetableRequest
from . import ignore_invalid_elvira_cookie


class Elvira:
    async def __aenter__(self):
        self.api_client = elvira_client.ApiClient()
        self.api_instance = elvira_client.DefaultApi(self.api_client)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.api_client.close()

    async def get_station_list(self):
        return await self.api_instance.get_station_list()

    async def get_timetable(
        self,
        station_number_code: str,
        travel_date=datetime.now(timezone.utc),
        min_count=0,
        max_count=9999999,
    ):
        timetable_request = TimetableRequest(
            type="StationInfo",
            travel_date=travel_date.isoformat(),
            station_number_code=station_number_code,
            min_count=str(min_count),
            max_count=str(max_count),
        )

        response = await self.api_instance.get_timetable(
            language="en", timetable_request=timetable_request
        )

        return response.station_scheduler_details
