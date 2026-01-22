from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.18",
    "username": "rolivagyok",
    "password": "kiskacsa",
}

kapcsolat = ConnectHandler(**kapcsolo)
print(kapcsolat.find_prompt())

print(dir(kapcsolat))




kapcsolat.disconnect()