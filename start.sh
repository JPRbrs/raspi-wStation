#!/bin/bash

sudo gunicorn app:app -b 0.0.0.0:80 --workers 1 --log-level warning --log-file logs/gunicorn-errors.log --access-logfile logs/gunicorn-access.log  --name weather_station -p app.pid -D
