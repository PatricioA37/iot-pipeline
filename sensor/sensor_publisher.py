import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# Pines del HC-SR04
TRIG = 23
ECHO = 24

# Configuración GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Conexión MQTT
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    return distance

try:
    while True:
        dist = get_distance()
        client.publish("iot/proximity", round(dist, 2))
        print(f"Distancia: {dist:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Deteniendo")
    GPIO.cleanup()
