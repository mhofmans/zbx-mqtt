# ZBX-MQTT
A simple, yet functional, way to integrate devices that support MQTT to your Zabbix Server.
This script does not contain broker authentication. (I will add a second script including authentication soon)

# MQTT Broker
Make sure you have a MQTT Broker running. <a href="https://mosquitto.org">Mosquitto</a> is recommended.
By default the Mosquitto broker only allows localhost, make sure to change the Mosquitto configuration file.

# MQTT to Zabbix
Open the Python script ```zbxmqtt.py``` and set the variables.

```php
ZabbixServer="x.x.x.x" # zabbix ip
ZabbixPort=10050 # zabbix listening port default 10050
Broker="x.x.x.x" # broker ip
```

Run ZBXMQTT as you prefer. This script is responsible for receiving MQTT data and sending it to Zabbix server, so make sure it is running all the time.
It's recommended to run it as a service. If this is your preference, ```zbxmqtt.service``` is an example of configuration.
You can also run it in nohup or screen:
```
screen -S session_name
python script.py
Ctrl-A D
```
Reconnect to screen:
```
screen -r session_name
```
# Zabbix host configuration
* Create host
* Set type to Trapper
* Add an item including a unique key and set its type to float
* Save changes

Now we have created the host including our first item, we need to change one more thing.
Inside the ```zbxmqtt.py``` script we subscribe to a specific topic.
Make sure you change this to your ```hostname.itemkey``` which you just created.
You can also subscribe to all topics by changing this value to ```#```.
Subscribing to ```#``` gives you a subscription to everything except for topics that start with a ```$``` (these are normally control topics anyway).

```php
client.subscribe("host.itemkey")
```
