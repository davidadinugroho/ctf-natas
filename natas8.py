#!/usr/bin/env python3

import requests
import re
import binascii
import base64

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.t

source = url + '/index-source.html'
encoded_secret = '3d3d516343746d4d6d6c315669563362' # from source

secret = base64.b64decode(binascii.unhexlify(encoded_secret)[::-1])

data = {
    'secret': secret,
    'submit': 'submit'
}
response = requests.post(url, auth=(username, password), data=data)
content = response.text

flag = re.findall('Access granted. The password for natas9 is (.*)', content)[0]

print(flag)