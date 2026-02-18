from netmiko import ConnectHandler


login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        tftp_ip = input(f"Add meg az IP-t ami a tftp szerberhez tartozik:")
        fajlnev = input(f"Faljnev:")

        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])

        print(output)



except Exception as ex:
    print("Valami hiba van:", ex)
