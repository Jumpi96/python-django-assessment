#!/bin/bash

python manage.py migrate
python manage.py loaddata movie
echo "from django.contrib.auth.models import User; User.objects.create_superuser('developer', 'dev@nicasource.com', 'CHANGEME')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
