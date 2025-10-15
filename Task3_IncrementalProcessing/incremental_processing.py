from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'cdc-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


user_data = {}

print("Listening for CDC events...")

for message in consumer:
    event = message.value
    operation = event.get("op")      
    user_id = event.get("id")
    name = event.get("name", "")
    age = event.get("age", 0)

    if operation == "insert":
        user_data[user_id] = {"name": name, "age": age}
        print(f"Inserted: {user_id} -> {user_data[user_id]}")

    elif operation == "update":
        if user_id in user_data:
            user_data[user_id]["name"] = name
            user_data[user_id]["age"] = age
            print(f"Updated: {user_id} -> {user_data[user_id]}")
        else:
            print(f"Update ignored (ID {user_id} not found)")

    elif operation == "delete":
        if user_id in user_data:
            del user_data[user_id]
            print(f"Deleted: {user_id}")
        else:
            print(f"Delete ignored (ID {user_id} not found)")

    print("Current state:", user_data)
