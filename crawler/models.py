from django.db import models


class Schedule(models.Model):
    class ScheduleType(models.TextChoices):
        ARRIVAL = "arrival"
        DEPARTURE = "departure"

    type = models.CharField(max_length=50, choices=ScheduleType.choices)

    # Where
    station_name = models.CharField(max_length=100)
    station_code = models.CharField(max_length=50)

    # When
    scheduled_arrival = models.DateTimeField()
    scheduled_departure = models.DateTimeField()
    actual_or_estimated_arrival = models.DateTimeField(null=True)
    actual_or_estimated_departure = models.DateTimeField(null=True)

    # What
    train_name = models.CharField(max_length=50, null=True)
    train_number = models.CharField(max_length=50)
    train_id = models.CharField(max_length=50)
    relation_symbol = models.CharField(max_length=50, null=True)
    kind_name = models.CharField(max_length=50, null=True)

    # Start station
    start_station_name = models.CharField(max_length=100)
    start_station_code = models.CharField(max_length=50)
    start_station_id = models.PositiveIntegerField()

    # End station
    end_station_name = models.CharField(max_length=100)
    end_station_code = models.CharField(max_length=50)
    end_station_id = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
