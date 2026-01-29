from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}

def mentes(ssh):
    ssh.save_config()

def jelszo(ssh):
    jelszo = input("Kérek egy szép hosszú bonyolult jelszót: ")
    ssh.send_config_set(f"ena pass {jelszo}")











##############################################################################
#                                  PROGRAM                                   #
##############################################################################

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 2. f
        print(kapcsolat.find_prompt())       
        
        # 3. f
        mentes(kapcsolat)
        
        valasz = kapcsolat.send_command("sh start")
        if "not present" not in valasz:
            print("Muxik a mentes")
        else:
            print("Nem mentett")
        

        #4. f
        jelszo(kapcsolat)

        print(kapcsolat.send_command("sh run | include enable"))



except Exception as ex:
    print("Valami hiba van:", ex)
