FROM python:3.8-slim

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]