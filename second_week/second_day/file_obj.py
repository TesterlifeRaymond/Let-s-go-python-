
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-18 06:01:48
# @FileName:  file_obj.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-18 06:41:52
"""
import json
import requests

# w 写入
# r 读取
# a 是添加
file = open('file/text.log', 'a', encoding='utf-8')
file.write('今天是星期二\n')
file.write('今天有雾霾\n')
file.close()

with open('file/text.log', 'r', encoding='utf-8') as file:
    print(file.readlines())

with open('file/text.log', 'w', encoding='utf-8') as file:
    file.write('今天好像特别热？\n')
    value = ('the answer', 42)
    value = str(value) + '\n'
    file.write(value)
    print(file.isatty())
    print(file.truncate())
    # file.seek

content = requests.get('http://img.blog.csdn.net/20160125135944363').content
# bytes 类型的数据流
with open('file/img.png', 'wb') as img:
    img.write(content)

# with open('file/img.png', 'rb') as img:
#     print(img.read())

# content = requests.get("http://124.202.166.51/file3.data.weipan.cn/57840318/ee19d3d13236345b0bc6
# ef534b4650d7faccd6e5?ip=1492468507,121.69.255.251&ssig=wMr1RswuwB&Expires=1492469107&KID=sae,l30zoo1wmz&fn=Python%20web%E6%A1%86%E6%9E%B6.Flask%E4%B8%AD%E6%96%87%E6%89%8B%E5%86%8C.pdf&skiprd=2&se_ip_debug=121.69.255.251&corp=2&from=1221134&wshc_tag=0&wsts_tag=58f53e6c&wsid_tag=e83151f&wsiphost=ipdbm").content
# with open('file/flask.pdf', 'wb') as pdf:
#     pdf.write(content)


_json = {
    "name": "Ray",
    "sex": "male",
    "age": "22",
    "like": "something"
}
with open('file/userinfo.json', 'w') as file:
    json.dump(_json, file)

with open('file/userinfo.json', 'r') as file:
    print(json.loads(file.read()))
