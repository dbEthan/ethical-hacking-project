# Source used: https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from rich import print as rprint


def run(**args):
    rprint("[*] Scanning network.")

    request = ARP()

    request.pdst = '192.168.1.1/24'
    broadcast = Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    result = srp(request_broadcast, timeout=1, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    message = "Available devices in the network:\n"
    message += "IP" + " "*18+"MAC"
    for client in clients:
        message += "{:16}    {}".format(client['ip'], client['mac'])

    rprint(f" :blue: {message}")
    return message
