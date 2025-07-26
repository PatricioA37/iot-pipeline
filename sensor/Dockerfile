FROM python:3.9-slim

# Instalar compiladores y librerías necesarias para RPi.GPIO
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY sensor_publisher.py .

RUN pip install --no-cache-dir paho-mqtt RPi.GPIO

CMD ["python", "sensor_publisher.py"]
