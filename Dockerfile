ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8080


CMD gunicorn 'counter-service:app' --bind=0.0.0.0:8080
