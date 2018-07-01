#!/usr/bin/env python3

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

user = url + '/files/users.txt'
response = requests.get(user, auth=(username, password))
content = response.text

flag = re.findall('natas3:(.*)', content)[0]

print(flag)