from dotenv import load_dotenv
from kafka import KafkaConsumer
from app.repo.elastic_repo.insert_to_elastic import insert_many_descriptions
import json
import os


load_dotenv(verbose=True)

def consume_all_massages():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EMAILS_NAME'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='latest'
    )
    for message in consumer:
        print(message.value)
        insert_many_descriptions(message.value)
