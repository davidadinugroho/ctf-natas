#!/usr/bin/env python3

import requests
import re

username = 'natasX'
password = ''

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password))
content = response.text

print(content)