FROM debian:buster-slim

WORKDIR /postman_collection
ENV DEBUG 0
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm install
RUN npm install -g newman

CMD newman run https://www.getpostman.com/collections/5466fd583152d6defc4e
