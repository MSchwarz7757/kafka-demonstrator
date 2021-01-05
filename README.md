# kafka-demonstrator

## Division of tasks
Tobias: Python Flask website to generate example events</br>
Michel: Python Confluent-Kafka message delivery from Flask website to Kafka</br>
Johannes: Replication for Confluent-Kafka Messages</br>

## Docker Python-Kafka Container aufbauen und starten
```
docker build -t python-kafka:1.0 .
docker run -it -p 5000:5000 --net confluent-kafka_default --name python-kafka python-kafka:1.0
```

## Start the Docker-Compose
Line in Docker-Compose.yml:
```bash
KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:29092,PLAINTEXT_HOST://localhost:9092
```
was changed to:
```bash
KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:29092,PLAINTEXT_HOST://broker:9092
```
### create topic
```bash
docker-compose exec broker kafka-topics --create --topic vks --bootstrap-server broker:9092 --replication-factor 1 --partitions 1
```
### create consumer 
```bash
docker-compose exec schema-registry bash
kafka-avro-console-consumer --topic vks --bootstrap-server broker:9092 
```

### create producer
```bash
docker-compose exec schema-registry bash
kafka-avro-console-producer --topic vks --bootstrap-server broker:9092 --property value.schema="$(< /opt/app/schema/order_detail.avsc)"
```

### control-center visible here: 
```bash
http://localhost:9021
```

## Python-Script
Dont forget to change the network address for the Broker and the schema registry
```python
'bootstrap.servers': "172.XX.0.3:9092",
'schema.registry.url': "http://172.XX.0.4:8081",
```
Use this command to find the ip: Docker inspect container-name

## Create and Run Python Container:
```bash
docker build -t kafka-python:1.X .
docker run -it --net confluent-kafka_default kafka-python:1.1
```
### Python and Confluent-Kafka help
[Pip Package](https://pypi.org/project/confluent-kafka/)</br>
[Confluent Tutorial](https://kafka-tutorials.confluent.io/kafka-console-consumer-producer/kafka.html#initialize-the-project)</br>
[Confluent Python Code](https://github.com/confluentinc/confluent-kafka-python)</br>
