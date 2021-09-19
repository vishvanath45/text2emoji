FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /text2emoji
WORKDIR $APP_HOME
COPY . ./

RUN pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 0 --timeout 0 main:app