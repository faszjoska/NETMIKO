from netmiko import ConnectHandler


login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
       
        if len(kapcsolat.send_command("sh run | include enable pass")[-1]) >= 8:
            pass
        else:
            print("A privilegizált mód jelszó nem 8 karakter") 
            jelszo = input("Egy 8 karakteres jelszo-t adj meg:")
            kapcsolat.send_config_set(f"enable pass {jelszo}")
        
        konzol = kapcsolat.send_command("sh run | section line con")
        konzol = konzol.split("\n")
        print(konzol)

        """         
        elif kapcsolat.send_command("sh run | section line con") == 'password':
        len(kapcsolat.send_command()[-1]) < 8
        print("A konzol jelszó nem 8 karakter") 
        jelszo_con = input("Egy 8 karakteres konzol jelszo-t adj meg:")
        kapcsolat.send_config_set(f"enable pass {jelszo_con}")
        elif len(kapcsolat.send_command("sh run | section line vty")[4]) < 8:
            print("A vty jelszó nem 8 karakter") 
            jelszo_vty = input("Egy 8 karakteres VTY jelszo-t adj meg:")
            kapcsolat.send_config_set(f"enable pass {jelszo_vty}")
        elif len(kapcsolat.send_command("sh run | section line vty")[8]) < 8:
            print("A USER jelszó nem 8 karakter") 
            jelszo_user = input("Egy 8 karakteres USER jelszo-t adj meg:")
            kapcsolat.send_config_set(f"enable pass {jelszo_user}")


        kapcsolat.send_config_set("login block-for 60 attempts 3 within 600")
        
        tftp_ip = input(f"Add meg az IP-t ami a tftp szerverhez tartozik:")
        fajlnev = input(f"Faljnev:")

        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])

        print(output)
        """


except Exception as ex:
    print("Valami hiba van:", ex)
