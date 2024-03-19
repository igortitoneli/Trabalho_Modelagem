FROM python:3.11.3-slim-buster

RUN addgroup --system app && adduser --system --group app

COPY ../requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd git
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade --force-reinstall -r /app/requirements.txt
