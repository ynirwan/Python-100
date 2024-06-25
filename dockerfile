FROM python:3.4



ENV REFRESHED_AT 2020-07-01

ADD . /todolist
WORKDIR /todolist


RUN pip install --upgrade pip
RUN pip install Flask==0.10.1   validators ConfigParser pymongo redis   # mysql-connector  pymysql mysql-connector-python

RUN pip install -r requirements.txt




copy app /app

