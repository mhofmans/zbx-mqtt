import paho.mqtt.client as mqtt
import time
from pyzabbix import ZabbixMetric, ZabbixSender

ZabbixServer="x.x.x.x" # zabbix ip
ZabbixPort=10051 # zabbix listening port default 10050
Broker="x.x.x.x" # broker ip


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("p1monitor/phase/l1_v")
    client.subscribe("p1monitor/phase/l2_v")
    client.subscribe("p1monitor/phase/l3_v")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    packet = [
        ZabbixMetric(str(msg.topic).split('/')[1], str(msg.topic).split('/')[2], str(msg.payload.decode('utf-8'))), # this means we use host=phase itemkey=l1_v. Make sure to split with / when using p1monitor
    ]

    result = ZabbixSender(zabbix_server=ZabbixServer, zabbix_port=ZabbixPort, use_config=None, chunk_size=250).send(packet)
    print(result)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(Broker, 1883, 60) # broker ip

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
time.sleep(10) # 10s delay
mqttc.loop_forever()
