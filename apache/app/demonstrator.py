from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import socket

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
    }
  ]
}
"""

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

class Demonstrator:
    value_schema = avro.loads(value_schema_str)
    key_schema = avro.loads(key_schema_str)


    def __init__(self, broker_url, registry_url):
        self.broker_url = broker_url
        self.registry_url = registry_url

        self.avroProducer = AvroProducer({
            'bootstrap.servers': broker_url,
            'on_delivery': delivery_report,
            'schema.registry.url': registry_url,
        }, default_key_schema=self.key_schema, default_value_schema=self.value_schema)

        #value = {"ID": 2343438, "username": "Michel"}
        #key = {"ID": 2343438, "username": "Michel"}


    def checkLocation(self, loc,port):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = (loc, port)
        result_of_check = self.a_socket.connect_ex(location)
        if result_of_check == 0:
            print("Port is open")
        else:
            print("Port is not open")
        a_socket.close()

    def produceMessage(self,topic,value,key):
        print(self)
        print(topic)
        print(value)
        print(key)
        self.avroProducer.produce(topic=topic, value=value, key=key)
        self.avroProducer.flush()
