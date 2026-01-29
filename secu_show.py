from netmiko import ConnectHandler

def netmiko_show_version(kapcsolo):
    #kapcsolat = ConnectHandler(**kapcsolo)

    output = ""

    try:
        with ConnectHandler(**kapcsolo) as kapcsolat:
            output = kapcsolat.send_command("show version")       

    except Exception as ex:
        print("Valami hiba van:", ex)

def fajl_beolvas():
    try:
        with open("show_version.txt", "r", encoding="utf-8") as fajl:
            szoveg = fajl.read()    
    
    except IOError as ex:
        print(ex)

    return szoveg

#Milyen IOS verzio van a kapcsolon?

def version(verzio_info):
    elso_sor = verzio_info.split('\n')[0]

    r = elso_sor.split(",")

    verzio = r[1].strip().split(" ")[2].lstrip("(").rstrip(")")
    verzio += " " + r[2].strip().lstrip("Version ")

    return verzio 

#Hany ethernet int van?

def ethernet_interface_szama():
    pass


###############################################################################
#    PROGRAM
###############################################################################

output = ""

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.80",
    "username": "rolivagyok",
    "password": "kiskacsa",
}

#netmiko_show_version(kapcsolo)
#print(output)

verzio_info = fajl_beolvas()

print(version(verzio_info))