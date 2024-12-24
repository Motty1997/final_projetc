import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from app.kafka_consumer.consumer import consume_all_massages

load_dotenv(verbose=True)

app = Flask(__name__)

def init_topic(name: str, num_partitions: int, replication_factor: int):
    client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    topic = NewTopic(
        name=name,
        num_partitions=num_partitions,
        replication_factor=replication_factor
    )

    try:
        client.create_topics([topic])
    except TopicAlreadyExistsError as e:
        print(str(e))
    finally:
        client.close()

if __name__ == '__main__':
    init_topic(os.environ['TOPIC_EMAILS_NAME'], int(os.environ['NUM_PARTITIONS']), int(os.environ['REPLICATION_FACTOR']))
    consume_all_massages()
    app.run()