import os, sys
proj_path = "../"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "virtual_thermostat.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
import django
django.setup()
from server.models import Sensor, SensorLog
import paho.mqtt.client as mqtt_client


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    sensors = Sensor.objects.all()
    print("Sensor found " + str(len(sensors)))
    for sensor in sensors:
        print("Subscribing " + str(sensor.mqtt_topic))
        client.subscribe(sensor.mqtt_topic)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("/ESP_CORE/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    sensors = Sensor.objects.filter(mqtt_topic__exact=msg.topic)

    if sensors.count() > 0:
        print("Received update for sensor: " + sensors[0].name)
        log = SensorLog.objects.create(value = float(msg.payload), sensor = sensors[0])
        ciao = "Ciao"

def connect():
    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("openhabian", "enableopenhabian!")
    client.connect("openhabianpi", 1883, 60)
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    
connect()
