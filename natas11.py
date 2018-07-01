#!/usr/bin/env python3

import requests
import re

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org' % username

cookies = {
    'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'
}
response = requests.get(url, auth=(username, password), cookies=cookies)
content = response.text

flag = re.findall('The password for natas12 is (.*)', content)[0]

print(flag)