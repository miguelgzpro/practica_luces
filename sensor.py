import json
import paho.mqtt.client as mqtt
import time
import uuid
from datetime import datetime
import random

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "home/light_sensor"
PUBLISH_INTERVAL = 5

def generate_sensor_data():
    device_id = str(uuid.uuid4())
    sensor_data = {
        "device_id": device_id,
        "event_time": str(datetime.now()),
        "value": random.randint(30, 70),
        "accuracy": round(random.uniform(0.8, 1.0), 2)
    }
    return sensor_data

def publish_sensor_data(client):
    while True:
        sensor_data = generate_sensor_data()
        client.publish(MQTT_TOPIC, json.dumps(sensor_data))
        print(f"Published: {json.dumps(sensor_data)}")
        time.sleep(PUBLISH_INTERVAL)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Connection failed with code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    publish_sensor_data(client)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.disconnect()
