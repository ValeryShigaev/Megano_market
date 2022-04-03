#!/bin/bash
rm -rf db.sqlite3 && \
python manage.py makemigrations && \
python manage.py migrate && \

python manage.py new_site_name && \

python manage.py loaddata fixtures/profiles_app_groups.json &&\
python manage.py loaddata fixtures/profiles_app_users.json &&\
python manage.py loaddata fixtures/profiles_app_social.json &&\

python manage.py loaddata fixtures/discounts_app.discountcategory &&\
python manage.py loaddata fixtures/discounts_app.discount	&& \
python manage.py collectstatic --no-input && \
python manage.py runserver 0.0.0.0:8000
