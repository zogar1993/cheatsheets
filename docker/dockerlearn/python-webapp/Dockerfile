FROM python:3.9-rc-alpine

RUN pip install django
#RUN apt-get update && apt-get install python3-django

WORKDIR /app

COPY app/ .

CMD python manage.py runserver 0.0.0.0:1322

EXPOSE 1322

