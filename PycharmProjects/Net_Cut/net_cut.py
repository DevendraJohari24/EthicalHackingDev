#!/usr/bin/env python

# USE SOME COMMANDS IN TERMINAL FIRST - : "iptables -I FORWARD -j NETQUEUE --queue-num 0"

#INSTALL MODULE "NETFILTERQUEUE" to access the above queue created using command.
#Step1 : apt install python3-pip git libnfnetlink-dev libnetfilter-queue-dev // in kali installation of netfilterqueue
#Step2 : pip3 install -U git+https://github.com/kti/python-netfilterqueue

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop() #The packet is trapped using this
    #packet.accept() #packet is forward to the destination

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)# 0 is queue no used in above command
queue.run()




