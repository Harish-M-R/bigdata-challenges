# Task 2: Real-Time Data Streaming Challenge

## Objective
Implement a Kafka Producer-Consumer system in Python to simulate real-time sensor data streaming and basic stream processing.

---

## Steps to Run (Copy-Paste Ready)

# 1. Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# 2. Start Kafka Broker
bin/kafka-server-start.sh config/server.properties

# 3. Create Kafka Topic
bin/kafka-topics.sh --create \
    --topic sensor-data \
    --bootstrap-server localhost:9092 \
    --partitions 1 \
    --replication-factor 1

# 4. Install Python dependency
pip install kafka-python

# 5. Run Producer (generates sensor data)
python Task2_RealTimeStreaming/producer.py

# 6. Run Consumer (reads and prints data)
python Task2_RealTimeStreaming/consumer.py

# 7. Run Stream Processor (calculates rolling average)
python Task2_RealTimeStreaming/stream_processing.py

---

## Files
- `producer.py` → Produces random sensor readings (temperature, humidity).
- `consumer.py` → Consumes and displays raw messages.
- `stream_processing.py` → Consumes data and calculates rolling averages.

---

## Tools Used
- Apache Kafka (real-time data streaming)
- Python (`kafka-python` library)
