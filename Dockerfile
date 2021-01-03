FROM python:3.6

RUN pip install requests requests_oauthlib confluent-kafka confluent-kafka[avro]

COPY ./order_detail.avsc ./order_detail.avsc
ADD confluent.py /
CMD python3 confluent.py
