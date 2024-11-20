# Train schedule crawler

Fetches timetables for the given station codes
and saves them to the database for later analysis.

Designed to be run periodically, i.e. as a cron job.

## Usage

    ./manage.py fetch_timetables --station-codes 005510470 005510454