from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import socket

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
location = ("172.22.0.3", 9092)
result_of_check = a_socket.connect_ex(location)
if result_of_check == 0:
   print("Port is open")
else:
   print("Port is not open")

a_socket.close()


value_schema_str = """
{
  "type": "record",
  "namespace": "VKSDemo",
  "name": "OrderDetail",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "username",
      "type": "string",
      "doc": "The users name"
    },
    {
      "name": "message",
      "type": "string",
      "doc": "The message which is sent"
    }
  ]
}
"""

key_schema_str = """
{
  "type": "record",
  "namespace": "VKSDemo",
  "name": "OrderDetail",
  "fields": [
    {
      "name": "ID",
      "type": "long",
      "doc": "The user ID"
    },
    {
      "name": "username",
      "type": "string",
      "doc": "The users name"
    },
    {
      "name": "message",
      "type": "string",
      "doc": "The message which is sent"
    }
  ]
}
"""
value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)


value = {"ID":2343438,"username":"Michel","message":"Das ist ein Test"}
key = {"ID":2343438,"username":"Michel","message":"Das ist ein Test"}


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


avroProducer = AvroProducer({
    'bootstrap.servers': "172.22.0.3:9092",
    'on_delivery': delivery_report,
    'schema.registry.url': "http://172.22.0.4:8081",
    }, default_key_schema=key_schema, default_value_schema=value_schema)


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


msg = {"ID":2343438,"username":"Michel","message":"Das ist ein Test2"}


avroProducer.produce(topic='vks', value=value, key=key)
avroProducer.produce(topic='vks', value=value, key=key)
avroProducer.flush()

