
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-27 06:07:52
# @FileName:  _requests.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-27 07:12:17
"""

import requests

response = requests.get('http://testerlife.com')
print(response)
#   http method get

response = requests.post('http://testerlife.com')
print(response)
# http method post


body = {'key1': 'value1', 'key2': ['value2', 'value2.1', 'value2.2']}
# k1=v1&k2=v2, params=body
response = requests.get("http://httpbin.org/get", params=body)
当body的值为None时， 是不会被添加在params中的
value 可以是一个list类型的数据 进行传递
print(response.url)
print(response.text)
# text : 返回字符串类型

print(response.content)
# content : 以二进制的形式 返回bytes类型

print(response.json())
r.json() 返回一个字典类型的数据， 如果返回数据不是json结构，则会跑出ValueError异常

img_url = 'http://testerlife.com/img/head.jpg'
image = requests.get(img_url)

with open('head.jpg', 'wb') as file:
    for chunk in image.iter_content(chunk_size=1024):
        file.write(chunk)


response = requests.get('https://github.com/timeline.json', stream=True)
print(response.raw.read(20))
