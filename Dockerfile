FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /dentistAPI
WORKDIR /dentistAPI
ADD . /dentistAPI/
RUN pip install -r requirements.txt