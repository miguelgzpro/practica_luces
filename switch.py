import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_TOPIC = "home/light_sensor"

def process_sensor_data(sensor_data):
    value = sensor_data['value']
    accuracy = sensor_data['accuracy']

    if value < 50 and accuracy > 0.9:
        return "Las luces se encenderán."
    else:
        return "Las luces serán apagadas."

def on_message(client, userdata, msg):
    sensor_data = json.loads(msg.payload)
    result = process_sensor_data(sensor_data)
    print(result)

def setup_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.subscribe(MQTT_TOPIC)
    client.loop_forever()

if __name__ == "__main__":
    setup_mqtt()
