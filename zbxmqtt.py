import paho.mqtt.client as mqtt
from pyzabbix import ZabbixMetric, ZabbixSender

ZabbixServer="x.x.x.x" # Zabbix ip
ZabbixPort=10051 # Zabbix listening port default 10050
Broker="x.x.x.x" # Broker ip


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("host.itemkey")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    packet = [
        ZabbixMetric(str(msg.topic).split('.')[0], str(msg.topic).split('.')[1], str(msg.payload.decode('utf-8'))),
    ]

    result = ZabbixSender(zabbix_server=ZabbixServer, zabbix_port=ZabbixPort, use_config=None, chunk_size=250).send(packet)
    print(result)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(Broker, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()
