FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="config.settings.production"

WORKDIR /code

COPY requirements/base.txt requirements/dev.txt requirements/production.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r production.txt

COPY . /code

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]