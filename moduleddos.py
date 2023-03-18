from telnetlib import IP
import pcapy, random
from scapy.all import *
from netfilterqueue import NetfilterQueue
import sys


TCP_PROTO = 6
ipAddress = []

def scanPkt(packet):

    tcpPkt = IP(packet.get_payload())
    fullpayload = bytes(tcpPkt[TCP].payload).decode('UTF8','replace')

    if tcpPkt.proto == TCP_PROTO:
        sourceIP = tcpPkt[IP].src
        #Checking if there is a SYN flag in the packet
        if tcpPkt[TCP].flags == 'S':
            print("SYN packet detected " + sourceIP + " sequence: " + str(tcpPkt[TCP].seq) + " Ack: " + str(tcpPkt[TCP].ack))
            #Some TCP flooding packets contain raw useless data in form from X
            if 'XXXXXXXXXXXXXXXXX' in fullpayload:
                print("Found possible SYN FLOOD ATTACK")
                packet.drop()
                return

            #Check how many times the same Ip address has sent a SYN packet
            for pkt in ipAddress:
                if pkt["IP"] == sourceIP:
                    pkt["Ammountconnected"] = pkt["Ammountconnected"] + 1
                    if pkt["Ammountconnected"] > 5:
                        packet.drop()
                        return        

            ipAddress.append(
            {"IP": sourceIP, "sequence": tcpPkt[TCP].seq, "Ammountconnected": 1})

        #Checking if there is a ACK flag in the packet
        elif tcpPkt[TCP].flags == 'A':
            print("ACK packet detected " + sourceIP + " sequence: " + str(tcpPkt[TCP].seq) + " Ack: " + str(tcpPkt[TCP].ack))
            for pkt in ipAddress:
                if pkt["IP"] == sourceIP:
                    if (tcpPkt[TCP].seq -1) == pkt["sequence"]:
                        pkt["Ammountconnected"] = 1

    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(3, scanPkt)

try:
    print("Running DDoS module" +str(nfqueue.get_fd()))
    nfqueue.run()
except KeyboardInterrupt:
    print('\nStopping DDoS module')
