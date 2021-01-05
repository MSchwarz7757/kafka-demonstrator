from confluent_kafka.avro import AvroProducer
import socket



def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

class KafkaProducer:

    def __init__(self, b_loc, b_port, r_loc, r_port,key_schema,value_schema):
        self.b_loc = b_loc
        self.b_port = b_port
        self.b_loc = r_loc
        self.b_loc = r_port
        self.value_schema = value_schema
        self.key_schema = key_schema

        self.avroProducer = AvroProducer({
            'bootstrap.servers': b_loc+":"+b_port,
            'on_delivery': delivery_report,
            'schema.registry.url': "http://"+r_loc+":"+r_port,
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
        self.avroProducer.produce(topic=topic, value=value, key=key)
        self.avroProducer.flush()
