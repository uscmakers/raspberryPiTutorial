import paho.mqtt.client as mqtt
import time

from gpiozero import LightSensor
ldr = LightSensor(4)

client = mqtt.Client()
client.connect("eclipse.usc.edu", 1883, 60)

while True:
    if ldr.value > 0.75:
        client.publish("makers", "on")
        print("dark")
    else:
        client.publish("makers", "off")
        print("bright")
        
    time.sleep(0.5)
