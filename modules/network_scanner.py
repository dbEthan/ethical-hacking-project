# Source used: https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/
import scapy.all as scapy
from rich import print as rprint


def run(**args):
    rprint("[*] Scanning network.")

    request = scapy.ARP()
    message = "List of clients:\n"

    request.pdst = 'x'
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout=1)[0]
    for element in clients:
        message += f"{element[1].psrc}\t{element[1].hwsrc}\n"
