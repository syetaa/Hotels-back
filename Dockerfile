FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--ssl-keyfile", "./key.pem", "--ssl-certfile", "./cert.pem",  "--host", "0.0.0.0", "--port", "80", "--reload" ]
