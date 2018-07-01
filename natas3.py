#!/usr/bin/env python3

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

# robot = url + '/robots.txt'
# response = requests.get(robot, auth=(username, password))
# content = response.text

secret = url + '/s3cr3t/users.txt'
response = requests.get(secret, auth=(username, password))
content = response.text

flag = re.findall('natas4:(.*)', content)[0]

print(flag)