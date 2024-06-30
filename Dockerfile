FROM python:alpine3.19

WORKDIR /app

RUN apk update && \
    apk add \
    curl \
    unzip \
    wget \
    xvfb


RUN apk add chromium \
    chromium-chromedriver
    
ENV FLASK_APP=back.py

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN chromium --version && chromedriver --version

EXPOSE 5000

COPY . .

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "back:app"]

