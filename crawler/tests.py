from django.core.management import call_command
from django.test import TestCase

from .models import Schedule


class Test(TestCase):
    def test_fetch_timetables(self):

        call_command("fetch_timetables", station_codes=["005510470", "005510454"])
        call_command("fetch_timetables", station_codes=["005510470", "005510454"])

        self.assertGreater(Schedule.objects.count(), 0)

        for schedule in Schedule.objects.all():
            self.assertIsInstance(schedule.station_name, str)
