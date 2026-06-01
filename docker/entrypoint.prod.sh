#!/bin/sh


if [ -n "$POSTGRES_HOST" ]
then
    echo "Waiting for postgres ($POSTGRES_HOST:$POSTGRES_PORT)..."

    while ! nc -z "$POSTGRES_HOST" "${POSTGRES_PORT:-5432}"; do
      sleep 0.5
    done

    echo "PostgreSQL has been launched!"
fi


# applying migration
echo "*** Running applying migrations..."
#flask db migrate
flask db upgrade


# populating database
echo "*** Running populating database..."
python -c "from src.models._inserts import populate_films; populate_films()"


exec "$@"