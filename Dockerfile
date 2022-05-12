FROM python:3.8.6-slim

WORKDIR /framework

COPY . .
RUN pip install -r requirements.txt


ENTRYPOINT ["pytests"]
