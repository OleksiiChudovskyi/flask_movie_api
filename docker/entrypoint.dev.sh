#!/bin/sh

echo "*** Running applying migrations for Development (SQLite)..."
flask db upgrade

echo "*** Running populating database..."
python -c "from src.models._inserts import populate_films; populate_films()"

exec "$@"