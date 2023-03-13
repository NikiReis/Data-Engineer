import ipaddress

ip = '192.168.0.1'
new_ip = '192.168.0.0/24'

address = ipaddress.ip_address(ip)
network = ipaddress.ip_network(new_ip)
# network = ipaddress.ip_network(new_ip, strict = False)
print(address + 201)
print(network)


print('IP addresses in / {0/4/16/24/32} network\n')

for x in network:
    print(x)
