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

def konzol(ssh):
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
    
        
         


##############################################################################
#                                  PROGRAM                                   #
##############################################################################

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #1. f
        vlan(kapcsolat)

        print(kapcsolat.send_command("sh vlan brief"))
        #2. F
        konzol(kapcsolat)



except Exception as ex:
    print("Valami hiba van:", ex)
