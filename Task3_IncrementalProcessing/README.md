# Task 3: Incremental Data Processing with Change Data Capture (CDC)

## Objective
Simulate Incremental Data Processing using Kafka to capture database-like changes (Insert, Update, Delete) and maintain an up-to-date state.

---

## Steps to Run (Copy-Paste Ready)

# 1. Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# 2. Start Kafka Broker
bin/kafka-server-start.sh config/server.properties

# 3. Create Kafka Topic for CDC events
bin/kafka-topics.sh --create \
    --topic cdc-events \
    --bootstrap-server localhost:9092 \
    --partitions 1 \
    --replication-factor 1

# 4. Install Python dependency
pip install kafka-python

# 5. Run Incremental Processor (listens for CDC changes)
python Task3_IncrementalProcessing/incremental_processing.py

---

## Testing the Pipeline

# Open a new terminal and produce test CDC messages:

bin/kafka-console-producer.sh --topic cdc-events --bootstrap-server localhost:9092

# Paste JSON messages like:
{"op": "insert", "id": 1, "name": "Alice", "age": 25}
{"op": "insert", "id": 2, "name": "Bob", "age": 30}
{"op": "update", "id": 1, "name": "Alice Smith", "age": 26}
{"op": "delete", "id": 2}

---

## Example Output
Inserted: 1 -> {'name': 'Alice', 'age': 25}  
Inserted: 2 -> {'name': 'Bob', 'age': 30}  
Updated: 1 -> {'name': 'Alice Smith', 'age': 26}  
Deleted: 2  
Current state: {1: {'name': 'Alice Smith', 'age': 26}}

---

## Tools Used
- Apache Kafka
- Python (`kafka-python` library)
- Change Data Capture (CDC) Simulation
