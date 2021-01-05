from confluent_kafka.admin import AdminClient, NewTopic

def create_topic(topic1, topic2, topic3, partitions, replication):
    a = AdminClient({'bootstrap.servers': '172.22.0.4:9092'})

    new_topics = [NewTopic(topic, num_partitions=partitions, replication_factor=replication) for topic in [topic1, topic2, topic3]]

    fs = a.create_topics(new_topics)

    for topic, f in fs.items():
        try:
            f.result()
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))


#### Topics are created here