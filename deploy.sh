#!/bin/bash

# Exit on error
set -e

# Create and activate virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create logs directory if it doesn't exist
mkdir -p logs

# Start Gunicorn
gunicorn --config gunicorn_config.py mudakhir_app_backend.wsgi:application 