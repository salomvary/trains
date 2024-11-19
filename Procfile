release: python manage.py migrate
web: daphne delays.asgi:application --port $PORT --bind 0.0.0.0