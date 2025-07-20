from flask import Flask
from kafka import KafkaConsumer
import paho.mqtt.publish as publish
import threading
import json

app = Flask(__name__)

def consume_kafka():
    consumer = KafkaConsumer(
        'iot-temperatura',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        group_id='flask-agent',
        enable_auto_commit=True
    )
    for message in consumer:
        try:
            temperatura = float(message.value.decode())
            print(f"Temperatura recibida: {temperatura}")
            if temperatura > 30:
                print("¡Temperatura alta! Activando ventilador")
                publish.single("actuador/ventilador", "ON", hostname="mosquitto")
        except Exception as e:
            print("Error:", e)

@app.route("/")
def home():
    return "Flask Agent corriendo"

if __name__ == "__main__":
    threading.Thread(target=consume_kafka, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
