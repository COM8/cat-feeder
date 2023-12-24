import paho.mqtt.client as mqtt
from time import sleep
from typing import Any

class Hass:
    onMessage: Any
    mqttBroker: str
    mqttPort: int
    mqttTopic: str

    client: mqtt.Client

    def __init__(self, onMessage: Any, mqttBroker="10.0.10.34", mqttPort=1883, mqttTopic="home/kitchen/feeder"):
        self.onMessage = onMessage
        self.mqttBroker = mqttBroker
        self.mqttPort = mqttPort
        self.mqttTopic = mqttTopic
        self.client = mqtt.Client()

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()

    def __on_connected(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe(self.mqttTopic)

    def __on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        # print(f"message: {message}")
        self.onMessage(message)

    def connect(self, mqttUser: str, mqttPassword: str):
        self.client.username_pw_set(mqttUser, mqttPassword)
        self.client.on_connect = self.__on_connected
        self.client.on_message = self.__on_message

        self.client.connect(self.mqttBroker, self.mqttPort, 60)
        self.client.loop_start()

# hass: Hass = Hass()
# hass.connect(<someFunc>, "catfeedermqtt", "lol123")

# while True:
#     sleep(1)
