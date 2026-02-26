from netmiko import ConnectHandler
from getpass import getpass


login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.110",
    "username": "rolivagyok",
    "password": getpass(),
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
       
        if len(kapcsolat.send_command("sh run | include enable pass").split(' ')[-1]) < 8:
            print("A privilegizált mód jelszó nem 8 karakter") 
            jelszo = input("Egy 8 karakteres jelszo-t adj meg:")
            kapcsolat.send_config_set(f"enable pass {jelszo}")
        else:
            print("Enable jelszo OK")
           
            
        konzol = kapcsolat.send_command("sh run | section line con")
        konzol = konzol.split("\n")
        print(konzol)
        for i in konzol:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    print("Az konzol jelszó nem megfelelő hosszúságú.")
                    
                    ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló konzol jelszót: ")
                
                    while len(ujjelszo2) < 8:
                        ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line con 0" , f"password {ujjelszo2}"])
                    print("A jelszó beéllítása megtörtént.")
                else:
                    print("MEgfelelő az konzol jelszó")   
                
        vty = kapcsolat.send_command("sh run | section line vty 0 4")
        vty = vty.split("\n")
        print(vty)
        for i in vty:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    print("Az vty jelszó nem megfelelő hosszúságú.")
                    
                    ujjelszo3 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    while len(ujjelszo3) < 8:
                        ujjelszo3 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line vty 0 15" , f"password {ujjelszo3}"])
                    print("A jelszó beéllítása megtörtént.")
                else:
                    print("MEgfelelő az vty jelszó")    

        ena = kapcsolat.send_command("show run")
        if "username" in ena:
            val = kapcsolat.send_command("show run | include username").split('\n')
            print(val)
            
            for felh in val:
                if len(felh.split(' ')[-1]) < 8:
                    print(f"A {felh.split(' ')[1]} felhasználó jelszava nem megfelelő hosszúságú.")
                    usejelszo = input("Adj meg egy legalább 8 karakter hosszú jelszót: ")
                    while len(usejelszo) < 8:
                        usejelszo = input("Adj meg egy legalább 8 KARAKTER HOSSZÚ jelszót!: ")
                    osszerakott = ''
                    for szo in felh.split(' ')[:-2]:
                        osszerakott += szo + ' '
                    kapcsolat.send_config_set(f"{osszerakott}{usejelszo}")
                    print("A jelszó beállítása megtörtént.(°_,°)")  
                else: 
                    print(f"Jó a {felh.split(' ')[1]} jelszava.")
        
        kapcsolat.send_config_set("login block-for 60 attempts 3 within 600")
        
        tftp_ip = input(f"Add meg az IP-t ami a tftp szerverhez tartozik:")
        fajlnev = input(f"Faljnev:")

        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])

        print(output)
        


except Exception as ex:
    print("Valami hiba van:", ex)
