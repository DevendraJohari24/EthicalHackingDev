#!/usr/bin/env python


import requests



def request(url):
    try:
        get_response = requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("root/Downloads/subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = requests(test_url)
        #print (response.content())
        if response:
            print("[+] Discovered subdomain  -->" + test_url)