FROM postgres:9.6

ENV LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"

RUN apt-get update
RUN apt-get -y install python3 python3-pip libpq-dev

WORKDIR /db
COPY requirements.txt /db
RUN pip3 install -r requirements.txt
COPY db/ db/