from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from confluent_kafka.admin import AdminClient, NewTopic
import avro.schema
import socket


schema_login = avro.schema.parse(open("/var/www/apache-flask/app/schema/user_login.avsc", "rb").read())
schema_message = avro.schema.parse(open("/var/www/apache-flask/app/schema/user_message.avsc", "rb").read())
schema_mouse = avro.schema.parse(open("/var/www/apache-flask/app/schema/user_mouse.avsc", "rb").read())

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


class Demonstrator:

    def __init__(self, broker_urls, registry_url, topic):
        self.broker_urls = broker_urls
        self.registry_url = registry_url

        if topic == "login":
            self.value_schema = schema_login
            self.key_schema = schema_login
        if topic == "message":
            self.value_schema = schema_message
            self.key_schema = schema_message
        if topic == "mouse":
            self.value_schema = schema_mouse
            self.key_schema = schema_mouse

        self.avroProducer = AvroProducer({
            'bootstrap.servers': self.broker_urls,
            'on_delivery': delivery_report,
            'schema.registry.url': self.registry_url,
        }, default_key_schema=self.key_schema, default_value_schema=self.value_schema)

    def checkLocation(self, loc,port):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = (loc, port)
        result_of_check = self.a_socket.connect_ex(location)
        if result_of_check == 0:
            print("Port is open")
        else:
            print("Port is not open")
        a_socket.close()

    def produceMessage(self, topic, value, key):
        self.avroProducer.produce(topic=topic, value=value, key=key)
        self.avroProducer.flush()


    def createTopic(self, *topic1, partitions, replication):
        a = AdminClient({'bootstrap.servers': self.broker_url})

        new_topics = [NewTopic(topic, num_partitions=int(partitions), replication_factor=int(replication)) for topic in [topic1]]

        fs = a.create_topics(new_topics)

        for topic, f in fs.items():
            try:
                f.result()
                print("Topic {} created".format(topic))
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))
