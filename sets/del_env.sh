#!/bin/sh

echo "Unset ENVIRONMENTS ..."

unset FLASK_ENV

unset SECRET_KEY

unset POSTGRES_DB
unset POSTGRES_USER
unset POSTGRES_PASSWORD
unset POSTGRES_HOST
unset POSTGRES_PORT

echo "ENVIRONMENTS have been unset successfully"