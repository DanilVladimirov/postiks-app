FROM python:3.8-slim-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV DEBUG 0
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

RUN npm install -g newman

COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev
RUN pip install -r requirements.txt
ENV PORT 8000
ENV REDIS_URL=redis://:UnXMlKDUIPqJ9pYJXEnqNzFeR52bBLsP@redis-13885.c266.us-east-1-3.ec2.cloud.redislabs.com:13885

COPY . .


CMD gunicorn postiks.wsgi:application --bind 0.0.0.0:$PORT