
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-18 06:42:55
# @FileName:  try_and_excepy.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-18 20:43:58
"""
import sys
import json

while 1:
    try:
        user_input = int(input('please enter every numbers .... :'))
        break
    except ValueError as ve:
        print(' Oops ! That was no valid number. Try again...')

    except KeyboardInterrupt as kbi:
        break

try:
    with open('file/userinfo.json', 'r') as file:
        data = file.read()
    print(json.loads(data))
except Exception as ex:
    print(data)
    print(ex)


try:
    f = open('file/userinfo.json', 'r')
    s = f.readline()
    i = int(f.readline(s))
except Exception as ex:
    print(ex)


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
