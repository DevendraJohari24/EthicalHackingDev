#!/usr/bin/env python
#Regex using for string manipulation

import  requests

def Download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb")  as out_file:    #here "r" use for reading and "w" for wriitig and "rw" use for reading and writing
        out_file.write(get_response.content)

download("DOWNLOADING___URL")
