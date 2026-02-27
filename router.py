from netmiko import ConnectHandler
from getpass import getpass


login_adatok = {
    "device_type": "cisco_ios",
    "host": "172.162.110.13",
    "username": "rolivagyok",
    "password": "kiskacsa",
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:

        print(kapcsolat.send_command("sh ip ospf neighbor"))
        """ 
        ospf_az =  kapcsolat.send_command("sh run | include router ospf").split(" ")
        #print(ospf_az[-1])
        halozat_az = input("Adj meg egy hálózat címet amit szeretnél hirdetni:")
        print(kapcsolat.send_config_set([f"router ospf {ospf_az[-1]}", f"network {halozat_az} area 0"] ))

        savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
        while savszelesseg != 100 and savszelesseg != 1000 and savszelesseg != 10000: 
            savszelesseg = int(input("Adj meg egy referencia sávszélességet(100, 1000, 10000):"))
        print(kapcsolat.send_config_set([f"router ospf {ospf_az[-1]}", f"auto-cost reference-bandwidth {savszelesseg}"]))

        """     
        router_id = input("Kérek egy router azonositőt:")
        joe = True
        router_id = router_id.split(".")

        while len(router_id) != 4:
            router_id = input("Kérek egy router azonositót:")
        for i in router_id:
            if int(i) <= 255:
                joe
            elif i[-1] == ".":
                joe = False
            
            if joe:
                print(i)
                
        print(router_id)

       
       

        


except Exception as ex:
    print("Valami hiba van:", ex)
