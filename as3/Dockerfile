# syntax=docker/dockerfile:1
FROM python:3.8.5-alpine3.12
WORKDIR /usr/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]