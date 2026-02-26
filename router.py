from netmiko import ConnectHandler
from getpass import getpass


login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:

       print(kapcsolat.send_command("sh ip ospf neighbor"))

       ospf_az =  kapcsolat.send_command("sh run | include router ospf").split(" ")
       #print(ospf_az[-1])
       halozat_az = input("Adj meg egy hálózat címet amit szeretnél hirdetni:")
       print(kapcsolat.send_config_set([f"router ospf {ospf_az[-1]}", f"network {halozat_az} area 0"] ))

       savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
       while savszelesseg != 100 or 1000 or 10000: 
           savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
       kapcsolat.send_config_set[f"routert ospf {ospf_az[-1]}", f"auto-cost reference-bandwidth {savszelesseg}"]

       
       

        


except Exception as ex:
    print("Valami hiba van:", ex)
