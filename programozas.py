from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
        
        #Felhasználó felvitel
        while True:
            felhasznalo = input("Add meg a felhasználó nevét (vagy 'EXIT' a kilépéshez): ")
            if felhasznalo.upper() == "EXIT":
                print("Kilépés a felhasználók felviteléből...")
                break
            jelszo = input("Add meg a jelszót: ")
            jogosultság = input("Admin felhasználó (I/N): ").upper()
            while jogosultság not in ["I", "N"]:
                jogosultság = input("Hibás bemenet! Kérlek add meg helyesen (I/N): ").upper()
            if jogosultság == "I":
                jogosultság_szint = "privilege 15"
            else:
                jogosultság_szint = "privilege 1"  
            parancs = f"username {felhasznalo} {jogosultság_szint} password {jelszo}"
            kapcsolat.send_config_set(parancs)
            print(f"Felhasználó ({felhasznalo}) sikeresen hozzáadva.")
        
        
        print(kapcsolat.send_command("sh ver | include uptime"))
        hostname = kapcsolat.send_command("sh run | include hostname")
        hostname = hostname.split(" ")
        with open (f"konfiguráció{hostname[1]}.txt", "w", encoding="utf-8") as celfile:
                celfile.write(kapcsolat.send_command("sh run"))
        
        tftp_ip = input(f"Add meg az IP-t ami a tftp szerverhez tartozik:")
        fajlnev = input(f"Faljnev:")
        mentes = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        



except Exception as ex:
    print("Valami hiba van:", ex)