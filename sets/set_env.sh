#!/bin/sh

echo "Set ENVIRONMENTS ..."

export FLASK_ENV=$"production"

export POSTGRES_DB=$"fm"
export POSTGRES_USER=$"postgres"
export POSTGRES_HOST=$"db"
export POSTGRES_PORT=$"5432"

echo "ENVIRONMENTS have been set successfully"