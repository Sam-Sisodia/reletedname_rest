FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .  .

EXPOSE 8000
