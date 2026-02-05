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
    konzolOK = False
    hitelesites = False
    password = False

    print(konzol1)
    for i in konzol1:
        if parancsok[0] in i:
            for j in konzol1:
                if parancsok[1] == j:
                    konzolOK = True
                else:
                    hitelesites = True
        else:
            password = True
    
    if konzolOK:
        print("konzol ok")
    elif password:
        print("Nincs password")
    elif hitelesites:
        print("Nincs hitelesítés")
         


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
