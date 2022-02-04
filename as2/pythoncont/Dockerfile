ARG PYTHON_VERSION=3.8
FROM ubuntu:latest
FROM python:$PYTHON_VERSION
RUN pip3 install pytest
RUN pip3 install pylint
RUN pip3 install nbmake
WORKDIR /application