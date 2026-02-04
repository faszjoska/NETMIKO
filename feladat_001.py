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

def titkosit(ssh):
    ssh.send_config_set(f"service password-encryption")

def banner(ssh):
    ssh.send_config_set(f"banner motd -Jogosulatlanul bejelentkezni TILOS!-")

def rapid(ssh):
    ssh.send_config_set(f"span mode rapid-pvst")










##############################################################################
#                                  PROGRAM                                   #
##############################################################################

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 2. f
        print(kapcsolat.find_prompt())       
        
        #3. f
        mentes(kapcsolat)
        
        valasz = kapcsolat.send_command("sh start")
        if "not present" not in valasz:
            print("Muxik a mentes")
        else:
            print("Nem mentett")
        

        #4. f
        jelszo(kapcsolat)

        print(kapcsolat.send_command("sh run | include enable"))

        #5. f
        titkosit(kapcsolat)

        print(kapcsolat.send_command("sh run | include enable"))

        #6. f
        banner(kapcsolat)

        print(kapcsolat.send_command("sh run | include banner"))
        print(kapcsolat.send_command("sh run | include password"))

        #7. f
        rapid(kapcsolat)

        print(kapcsolat.send_command("sh run | include spanning-tree"))

        try:
            with open("konfig-mentve.txt", "w", encoding="utf-8")as cel:
                cel.write(kapcsolat.send_command("sh run"))

        except IOError as ex:
           print("Valami hiba van:", ex) 

except Exception as ex:
    print("Valami hiba van:", ex)
