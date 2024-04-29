#!/bin/bash
echo "Creating Migrations..."
python mysite/manage.py makemigrations hello_world
echo ====================================

echo "Starting Migrations..."
python mysite/manage.py migrate
echo ====================================

echo "Starting Server..."
python mysite/manage.py runserver 0.0.0.0:8000