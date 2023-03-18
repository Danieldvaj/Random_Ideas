from scapy.all import *
import os

synPacketDict = {}
sourceDict = {}

def pkt_sniffer(pkt):
    src = pkt.sprintf("%IP.src%")
    dst = pkt.sprintf("%IP.dst%")
    flags = pkt.sprintf("%TCP.flags%")

    if flags == 'S':
        packet_todict(dst, src)



def packet_todict(dst, src):
    if ("192.168" in dst)or(dst.startswith("10.")) or (dst.startswith("172.")):
        if dst in synPacketDict:
            synPacketDict[dst] += 1
            sourceDict[dst] = src
        else:
            synPacketDict[dst] = 1
            sourceDict[dst] = src

    if synPacketDict[dst] > 5:
        print("Possible SYN FLOOD ATTACK")
        print(src)
        os.system("tcpkill host " + src)
        os.system("sudo iptables -I INPUT -s + " + src + " -j DROP")
        os.system("sudo iptables -I OUTPUT -d " + src +" -j DROP")
        print("SYN FLOODER DETECTED, DROPPING PACKETS FROM " + src)
    

sniff(prn=pkt_sniffer, filter="tcp", store=0)
