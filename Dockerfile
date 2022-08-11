FROM ubuntu:latest
RUN date
RUN apt-get update
RUN apt-get install git python3-pip -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
