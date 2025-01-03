# Generated by Django 5.1.3 on 2024-12-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crawler", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="end_station_code",
            field=models.CharField(default="n/a", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedule",
            name="end_station_id",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedule",
            name="end_station_name",
            field=models.CharField(default="n/a", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedule",
            name="start_station_code",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedule",
            name="start_station_id",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedule",
            name="start_station_name",
            field=models.CharField(default="n/a", max_length=100),
            preserve_default=False,
        ),
    ]
