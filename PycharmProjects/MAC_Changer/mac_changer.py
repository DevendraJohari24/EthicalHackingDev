#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface",dest = "interface", help="Interface to change its MAC ")
    parser.add_option("-m" , "--mac",dest = "new_mac", help="New MAC Address ")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an inteface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify new MAC , use --help for more info ")
    return options


def change_mac(interface , new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call("sudo ifconfig " + interface + " down", shell=True)
    subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("sudo ifconfig " + interface + " up", shell=True)
    subprocess.call("sudo ifconfig ", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not read MAC Address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac :
    print("[+] MAC ADDRESS WAS SUCCESSFULLY CHANGE TO " + current_mac)
else :
    print("[-] MAC ADDRESS DID NOT CHANGE ")





