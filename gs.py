import ipaddress

prefix_input = input("Add meg a prefixet (pl. /24): ")
prefix = prefix_input.replace("/", "")

# Prefix → Subnet mask
network = ipaddress.IPv4Network(f"0.0.0.0/{prefix}")
subnet_mask = str(network.netmask)

print(f"A subnet mask: {subnet_mask}")
print(network)