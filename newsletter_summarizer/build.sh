#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Optionally create superuser (this will not stop the build if it fails)
if true; then
  python manage.py createsuperuser --no-input --email "admin@example.com" --username "admin" || true
fi
