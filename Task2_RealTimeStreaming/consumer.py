from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(f"Consumed: {message.value}")
