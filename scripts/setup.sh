#!/bin/bash

python3 -m pip install poetry
poetry install
docker-compose up -d
sleep 1  # Let the DB start up
poetry run alembic upgrade head
