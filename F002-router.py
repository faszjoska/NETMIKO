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

        

        """
        hostname = input("Add meg az eszkösz nevét:")
        kapcsolat.send_config_set(f"hostname {hostname}")

        uptime = kapcsolat.send_config_set("do sh ver")
        uptime = uptime.split("\n")
        uptime_ido = ""

        for i in uptime:
            if i.startswith(f"{hostname} uptime is"):
                uptime_ido = i

        print(uptime_ido)

        kapcsolat.send_config_set(["int g0/0/1.11", "encapsulation dot1Q 11", "ip addr 192.168.11.11 255.255.255.0", "no sh", "int g0/0/1.13", "encapsulation dot1Q 13", "ip addr 192.168.13.13 255.255.254", "no sh"])
        vlan_id = int(input("Add meg az uj vlan roas interfész azonosítóját (2-1001):"))
        ip = input("Adj meg neki egy ip-t:")
        prefix_input = input("Add meg a prefixet (pl. /24): ")
        prefix = prefix_input.replace("/", "")
        network = ipaddress.IPv4Network(f"0.0.0.0/{prefix}")
        subnet_mask = str(network.netmask)

        
        while vlan_id < 2 or vlan_id >1001:
            vlan_id = int(input("Add meg az uj vlan roas interfész azonosítóját (2-1001):"))
        
        kapcsolat.send_config_set([f"int g0/0/1.{vlan_id}", f"encapsulation dot1Q {vlan_id}", f"ip addr {ip} {subnet_mask}", "no sh"])
        
        
        tftp_ip = input(f"Add meg az IP-t ami a tftp szerverhez tartozik:")
        fajlnev = input(f"Faljnev:")
        mentes = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])

        # Parancs futtatása, ami kilistázza az interfészeket
        output = kapcsolat.send_command("show ip interface brief")
        
        eredmenyek = []
        
        # A kimenet soronkénti feldolgozása
        for line in output.splitlines():
            # Sor szétbontása szavakra
            parts = line.split()
            if not parts:
                continue
                
            interface_name = parts[0]
            
            # Megvizsgáljuk, hogy alinterfész-e (van benne pont) 
            # és megfelel-e az általad megadott g0/0/1 (vagy G0/1) feltételnek
            if "." in interface_name and ("0/0/1." in interface_name or "0/1." in interface_name):
                
                # A képen látható formátum eléréséhez a "GigabitEthernet"-et "G"-re cseréljük
                short_int = interface_name.replace("GigabitEthernet", "G").replace("gigabitethernet", "G")
                
                # A VLAN ID a pont utáni rész
                vlan_id = short_int.split(".")[1]
                
                eredmenyek.append((short_int, vlan_id))

                           
                
        # 2. Táblázat formázása és kiírása a csatolt minta alapján
        print("\n")
        print(f"{'Alinterface ID':<15} {'VLAN ID'}")
        print("-" * 35)
        for alint, vlan in eredmenyek:
            # A <15 balra igazítja a szöveget 15 karakter szélességben
            print(f"{alint:<15} {vlan}")

        
        loopback = int(input("Add meg a loopback interfész számát:"))
        loopback_ip = (input("Loopback IP címe:"))
        prefix_input_loopback = input("Add meg a prefixet (pl. /24): ")
        prefix_loopback = prefix_input_loopback.replace("/", "")
        network_loopback = ipaddress.IPv4Network(f"0.0.0.0/{prefix_loopback}")
        subnet_mask_loopback = str(network_loopback.netmask)

        kapcsolat.send_config_set([f"int loopback {loopback}", f"ip addr {loopback_ip} {subnet_mask_loopback}", "no sh"])
        """
        

except Exception as ex:
    print("Valami hiba van:", ex)
