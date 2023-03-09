FROM python:3.10-slim

COPY req.txt .

RUN python3 -m pip install -r req.txt

COPY . /datecheck-api

CMD python3 -m datecheck-api