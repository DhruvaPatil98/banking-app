FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY . /code/
WORKDIR /code

