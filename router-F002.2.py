from netmiko import ConnectHandler
import ipaddress

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
        #1.F
        outpu = kapcsolat.send_command("sh ver | include uptime")
        outpu = outpu.split(' ')
        print(f"Az eszköz {outpu[-2]} {outpu[-1]} ideje müködik.\n")

        #2.F
        output = kapcsolat.send_command("sh ip int br")
        
        interfesz_adatok = output.split("\n")

        print("Lekapcsolt interfészek:")
        for interfesz in interfesz_adatok:
            if "down" in interfesz:
                print(f"\t {interfesz.split(' ')[0]}")

        #3.F
        if_letrehozas = [
            "int loopback 123"
            "description UNOZZUNK!!!!!!!!!!!!!!!!!!!!!!"
            'ip addr 152.122.45.12 255.255.255.0'
            'no sh'
        ]

        kapcsolat.send_config_set(if_letrehozas)

        if len(kapcsolat.send_command("sh ip int br | include Loopback123")) != 0:
            print("Sikerült az interfész létrehozása")

        #4.F

        lekerd = kapcsolat.send_command("show interface g0/0/0")
        
        print(f"A g0/0 interfész EIGRP érték számításban szereplő paramétereinek értékei:")
        for sor in lekerd.split("\n"):
            if "BW" in sor:
                adatok = sor.split(",")
                
                for adat in adatok:
                    if "BW" in adat:
                        print(f"\t Sávszélesség: {adat.split(" ")[-2:]}")
                    elif "DLY" in adat:
                        print(f"\t Késleltetés: {adat.split(" ")[-2:]}")
            elif "reliability" in sor:
                adatok = sor.split(",")
                
                
                for adat in adatok:
                    if "reliability" in adat:
                        print(f"\t Megbízhatóság: {adat.split(" ")[-1]}")
                        print(f"\t Terhelés:", end=" ")
                    elif "load" in adat:
                        print(f"{adat.split(" ")[-1]}", end=" ")
        

except Exception as ex:
    print("Valami hiba van:", ex)
