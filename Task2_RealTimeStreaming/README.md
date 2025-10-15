# Task 2: Real-Time Data Streaming

## Objective
Implement a Kafka Producer-Consumer system to simulate real-time sensor data streaming.

## Files
- `producer.py`: Generates random sensor data and pushes to Kafka topic `sensor-data`.
- `consumer.py`: Listens to Kafka topic and prints received messages.
- `stream_processing.py`: Consumes data and calculates rolling average of last 5 temperature values.

## Steps to Run
1. Start Zookeeper and Kafka:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
2.Create a topic:

bin/kafka-topics.sh --create --topic sensor-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


3.Run producer:

python producer.py


4.Run consumer:

python consumer.py


5.Run stream processing:

python stream_processing.py

Tools:

Apache Kafka

Python (kafka-python library)
