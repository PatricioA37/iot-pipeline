from flask import Flask, request
import paho.mqtt.client as mqtt

app = Flask(__name__)

mqtt_broker = "mosquitto"
mqtt_port = 1883
mqtt_topic = "iot/test"

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

@app.route('/')
def index():
    return "MQTT Flask Agent Activo"

@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    msg = data.get("message", "Hola IoT")
    client.publish(mqtt_topic, msg)
    return {"status": "mensaje enviado", "mensaje": msg}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
