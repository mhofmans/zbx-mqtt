# ZBXMQTT
A simple, yet functional, way to integrate devices that support MQTT to your Zabbix Server.
This script does not contain broker authentication. (I will add a second script including authentication soon)

# MQTT Broker
Make sure you have a MQTT Broker running. <a href="https://mosquitto.org">Mosquitto</a> is recommended.

# MQTT to Zabbix
Open the Python script ```zbxmqtt.py``` and set the variables.

```php
ZabbixServer="x.x.x.x" # Enter Zabbix server IP.
ZabbixPort= # Enter Zabbix server Port, default is 10051.

# Change the broker IP
```

Run ZBXMQTT as you prefer. This script is responsible for receiving MQTT data and sending it to Zabbix server, so make sure it is running all the time.
It's recommended to run it as a service. If this is your preference, ```zbxmqtt.service``` is an example of configuration.
