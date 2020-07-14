FROM python:3.9-rc-alpine

RUN apk add build-base && apk add postgresql-dev \
 && pip install django \
 && pip install psycopg2 \
 && pip install pygresql

WORKDIR /app

COPY app/ .

CMD python manage.py runserver 0.0.0.0:1322

EXPOSE 1322

