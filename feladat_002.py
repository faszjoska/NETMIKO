from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}

def vlan(ssh):
    parancsok = ["vl 10", "name Tanulo",
                 "vl 20", "name Oktato",
                 "vl 30", "name Pedagogus",
                 "vl 100", "name Ugyvitel",
                ]
    
    ssh.send_config_set(parancsok)

""" def konzol(ssh):
    konzolhitelesites = ssh.send_command("show run | section line con")
    parancsok = ["password", "login"]
    konzol1 = konzolhitelesites.split(" ")
   

    print(konzol1)
    if parancsok[0] in konzol1:
        if parancsok[1] == konzol1:
            print("konzol ok")
        else:
            print("Nincs hitelesítés")
    else:
        print("Nincs password")
    elif hitelesites:
        print("Nincs hitelesítés")
         

def int(ssh):
    interface = ssh.send_command("show run | include interface")
    interface = interface.split('\n')
    int2 = []
    int3 = []
    int4 = []
    int5 = []
    db = 0
    db2 = 0
    

    for i in interface:
        int2.append(i.split(' ')[1])
    for i in int2:
        int3.append(i.split('/')[0])
    for i in int3:
        int4.append(i[:-1])
    for i in int4:
        if "Ethernet" in i:
            int5.append(i)
    for i in int5:
        if "Fast" in i:
            db+=1
        if "Gigabit" in i:
            db2+=1
        
        
        
    print(f"FastEthernet port: {db} \nGigabitEthernet port: {db2}")

##############################################################################
#                                  PROGRAM                                   #
##############################################################################

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #1. f
        vlan(kapcsolat)

        print(kapcsolat.send_command("sh vlan brief"))
        
        int(kapcsolat)

except Exception as ex:
    print("Valami hiba van:", ex)
