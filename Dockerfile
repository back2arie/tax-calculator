FROM python:3.6.2

WORKDIR /usr/app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements/dev.txt

RUN apt-get update && apt-get install -y supervisor

RUN cp env.example .env

EXPOSE 8000

CMD []
