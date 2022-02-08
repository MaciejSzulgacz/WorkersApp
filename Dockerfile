# base img
FROM python:3.8.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /workersapp
WORKDIR /workersapp
ADD . /workersapp/

# install dependecies
COPY ./requirements.txt /workersapp/requirements.txt
RUN pip install -r requirements.txt

# copy project repository
COPY . /workersapp