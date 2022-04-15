FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Requirements/requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/curl

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]