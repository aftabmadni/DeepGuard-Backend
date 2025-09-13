#!/usr/bin/env bash
# build.sh

echo "Starting build process..."

# Install from requirements.txt (primary method)
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

echo "Build completed successfully!"