# kafka-demonstrator

## Start the Docker-Compose
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
With: Docker inspect container-name

## Create and Run Python Container:
```bash
docker build -t kafka-python:1.X .
docker run -it --net confluent-kafka_default kafka-python:1.1
```
### Python and Confluent-Kafka help
[Pip Package](https://pypi.org/project/confluent-kafka/)</br>
[Confluent Tutorial](https://kafka-tutorials.confluent.io/kafka-console-consumer-producer/kafka.html#initialize-the-project)</br>
[Confluent Python Code](https://github.com/confluentinc/confluent-kafka-python)</br>
