FROM python:3.6

RUN pip install requests requests_oauthlib confluent-kafka confluent-kafka[avro] flask

COPY . .
ADD confluent.py /
CMD python3 app.py
