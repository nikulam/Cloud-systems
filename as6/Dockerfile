FROM python:latest
WORKDIR /application
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload"]
