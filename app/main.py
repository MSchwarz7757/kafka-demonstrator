from kafka import KafkaProducer

import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers='172.19.0.3:29092')
producer.send('vks', {"ID": 2343438, "username": "Michel", "message": "Das ist ein Python test"})
print("is send")
#consumer = KafkaConsumer('vks', bootstrap_servers='172.19.0.3:29092')
#producer = KafkaProducer()
#for x in range(10):
    #x+=1
