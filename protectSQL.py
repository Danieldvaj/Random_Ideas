from dataclasses import field
from scapy.all import *
from  scapy_http.http import *
from netfilterqueue import NetfilterQueue
from urllib.parse import urlparse
from urllib.parse import parse_qs
import sys, os, json
import re
from datetime import datetime
import csv



TCP_PROTO = 6

blockedIPs = []
ipTables = []


def parsePacket(data):


    packetlist = []
    secondpacket =[]
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    sourceIP = data[IP].src
    sourcePRT = data[IP].sport
    destIP = data[IP].dst
    destPRT = data[IP].dport
    fullpayload = bytes(data[TCP].payload).decode('UTF8','replace')


    listparam = []
    payloaddec = bytes(data[TCP].payload).decode('UTF8','replace')
    params = re.findall('{(.+?)}', payloaddec)
    if len(params) != 0:
        paramsplitting = params[0].split(',')
        email = paramsplitting[0]
        password = paramsplitting[1]
        
        emailsplitting = email.split(':')
        passwordsplitting = password.split(':')
        emailstrip = emailsplitting[1][1:-1]
        
        passwordstrip = passwordsplitting[1].strip('\"')
       
        parsedparam ={ "Email" : str(emailstrip), "Password": str(passwordstrip), "Source Ip" :  str(sourceIP), "Source Port" : str(sourcePRT),  "Destination Ip" : str(destIP), "Destination Port" :  str(destPRT), "Time of Log": date}
        parsedlog ={ "Email" : str(emailstrip), "Password": str(passwordstrip), "Source Ip" :  str(sourceIP), "Source Port" : str(sourcePRT),  "Destination Ip" : str(destIP), "Destination Port" :  str(destPRT), "Full payload": fullpayload, "Time of Log": date}
        listparam.append(parsedparam)
        secondpacket.append(parsedlog)

        logSQL(listparam)
        normalLog(secondpacket)
    else:
        parsedlog ={"Source Ip" :  str(sourceIP), "Source Port" : str(sourcePRT),  "Destination Ip" : str(destIP), "Destination Port" :  str(destPRT), "Full payload": fullpayload, "Time of Log": date }
        secondpacket.append(parsedlog)
        normalLog(secondpacket)

def logSQL(sqlForm):
    SQLlist = ["=", "'", '\"', "|", "(", ")"]
    sqlHeader = ['Source Ip', 'Source Port', 'Destination Ip', 'Destination Port', 'Email', 'Time of Attack']
    with open("SQLINJECTIONLOG.csv", "a+") as sqlLog:
        for form in sqlForm:
                for sql in SQLlist:
                        if sql in form['Email']:
                                print("POSSIBLE SQL INJECTION DETECTED {TCP} " + form['Source Ip'] + ":" + form['Source Port'] + " -> " + form['Destination Ip'] + ":" + form['Destination Port'])
                                json.dump(sqlForm, sqlLog, indent = 2)
                                break
#                                sqllog.write("\n")

def normalLog(logging):
    with open("NORMALLOG.json", "a+") as normLog:
        for log in logging:
                json.dump(log, normLog, indent = 2)


def foundPacket(packet):

    ipHeader = IP(packet.get_payload())

    if ipHeader.proto == TCP_PROTO:

        sourceIP = ipHeader[IP].src
        destIP = ipHeader[IP].dst
        destPRT = ipHeader[IP].dport

        if len(ipHeader[TCP].payload) == 0:
                packet.accept()
                return
        parsePacket(ipHeader)

#        payloaddec = bytes(ipHeader[TCP].payload).decode('UTF8','replace')
#        print(payloaddec)


#        params = re.findall('{(.+?)}', payloaddec)
#        if params:
#                print(params)
#        else:
#                pass

#        if "POST" in payloaddec:
#                print(payloaddec)
#        else:
#                pass


    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(3, foundPacket)

try:
    print("Net filter active on " +str(nfqueue.get_fd()))
    nfqueue.run()
except KeyboardInterrupt:
    print('\nEnding session...')