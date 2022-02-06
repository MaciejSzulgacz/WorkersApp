FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /workersapp
WORKDIR /workersapp
ADD . /workersapp/
RUN pip install -r requirements.txt