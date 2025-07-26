FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-rpi.gpio
WORKDIR /app
COPY sensor_publisher.py .
RUN pip install paho-mqtt RPi.GPIO
CMD ["python", "sensor_publisher.py"]
