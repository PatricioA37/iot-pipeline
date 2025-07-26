import paho.mqtt.client as mqtt
import time
import random
import json

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker con código:", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("mosquitto", 1883, 60)

client.loop_start()

while True:
    fake_distance = round(random.uniform(5, 50), 2)
    message = json.dumps({"distance": fake_distance})
    rc, mid = client.publish("sensor/proximity", message)
    print(f"Publicado: {message}, rc: {rc}, mid: {mid}")
    time.sleep(2)
