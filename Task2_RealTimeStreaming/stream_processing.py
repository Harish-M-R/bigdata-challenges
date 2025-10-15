from kafka import KafkaConsumer
import json
import statistics


consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

temperatures = []

for message in consumer:
    data = message.value
    temperatures.append(data['temperature'])

    if len(temperatures) > 5:
        temperatures.pop(0) 
    avg_temp = statistics.mean(temperatures)
    print(f"Sensor ID: {data['sensor_id']} | Temp: {data['temperature']} | Rolling Avg: {avg_temp:.2f}")
