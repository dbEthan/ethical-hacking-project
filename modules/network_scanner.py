# Source used: https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from rich import print as rprint


def run(**args):
    rprint("[*] Scanning network.")

    request = ARP()
    message = "List of clients:\n"

    request.pdst = 'x'
    broadcast = Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = srp(request_broadcast, timeout=1)[0]
    for client in clients:
        message += f"{client.psrc}\t{client.hwsrc}\n"
