# Source used: https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/
from rich.progress import track
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from scapy.all import IP, TCP, sr1
from rich import print as rprint


def run(**args):
    rprint("[*] Scanning network.")

    hosts = []
    message = []
    message.append("Scapy:")
    rprint("[ :warning: ] Check scapy.")
    for i in range(1, 255):
        hosts.append("192.168.0." + str(i))
    for host in track(hosts, description="Scanning hosts..."):
        packet = IP(dst=host) / TCP(dport=80, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response is None:
            pass
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                message.append(host + " is up.")

    rprint(f" :blue: {message}")
    return message
