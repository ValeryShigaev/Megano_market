FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY entrypoint.sh /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh
COPY . /code
#RUN python manage.py loadscript --with_clear with_clear
ENTRYPOINT ["/code/entrypoint.sh"]