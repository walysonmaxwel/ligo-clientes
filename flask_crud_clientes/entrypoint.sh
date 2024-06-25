#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z postgres_db 5432; do
  sleep 1
done
echo "PostgreSQL started"

# Run migrations
echo "Running database migrations..."
flask db upgrade

# Start the Flask application
echo "Starting Flask application..."
exec flask run --host=0.0.0.0 --reload
