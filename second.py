
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-06 06:51:02
# @FileName:  second.py
# @Project: devops
# @Last Modified by:   jinjialiu
# @Last Modified time: 2017-04-10 07:36:32
"""
import json     # import 在python中 是引入包的模块

# 第二节， 数据类型

""" 首先， 我们在使用python的过程中， 会需要用到变量和不同数据类型的数据, 比如常见类型如下：
1: str
2: int
3: dict
4: list
5: float
6: json
7: bool
8: None
9: set
"""
print('123456', 123456)
print(type('123456'), type(123456))

print(isinstance('123456', str))
print(str == type('123'))
print(int("1") + 1)     # 格式统一为int类型 1 + 1
print("1" + str(1))     # 格式统一为str类型 "1" + "1"
print('1', "2", """3""")
print("hello" + "world" + "!")    # string字符串拼接
"""
好像数了一下，感觉好多啊。 那我们怎么理解这么多的不同的数据类型呢？
好像也很简单。

我们好像忘了点什么内容？？？
如何查看一个对象 or 变量 是什么类型？

1： type 可以获取当前对象的数据类型
    print(type(10000))

2： isinstance() 和楼上好像是类似的, 没错, 它返回的是一个bool, 而type返回的是类型结果
    print(isinstance(1, int))

不同的数据类型的特点

1: str  str类型的所有数据 都带有'str' or "str" 会被单引号或双引号引起来。
    print(type('1'), type('{1: 2, 3: 4}'), type('True'))

2: int  int类型 在python中其实可以理解为整数
    那如果我们输入一个负数呢？ print(type(-1)) 并不会有影响， 他依然属于整形

3: dict dict 也就是大家常提到的字典， 他的结构是{key: value} 以这样对应的形式存储起来的数据
比如:
    {"name": "Ray", "age": "30", "sex": "male"}
    str dict  import json
    json.dumps() ==> dict to str
    json.loads() ==> str to dict
    这是一个字典，他以key，value 的形式存储了用户的一些信息
    dir() 目标对象所包含的方法
这样的数据格式， 我们应该如何获取其中某个key的value？ 或者我们要增加或删除一些key value？

4: list list在其他语言中也被称为数组， 他的存储结构是[1, 2, 3, 4, 5, "abc", obj]

"""
__dict = {"key": "KEY", 1: 1, "name": "Ray", "age": 29}
print("isinstance(__dict, dict)", isinstance(__dict, dict))
print(__dict.get('age'), __dict.get('name'))


# {key-->("str" or 'int' or [list]) : value --> 任何对象}
# list 到底可不可以做dict 的key？？？

data = {"name": "Ray", "age": "30", "sex": "male"}  # 我们会发现dict的存储是无序的
# print(data)
# 首先，我们先获取name的值
keys = data.keys()  # 获取字典中全部的key
values = data.values()
all_item = data.items()     # 迭代器

# print("这是keys", keys)       # python3.6以前， dict 类型 是无序的
# print("这是values", values)
# print("这是全部的key and values :", all_item)


name = data.get('name')     # dict.get('key')
ray_name = data['name']     # dict['key']

# 他们两个的结果一样么？
# print(name, ray_name)
# 诶？ 好像是一样的？
# 那他们有什么区别呢？

# 我们看到了 ray_name 用data['Ray'] 来获取字典中的key对应的value的时候， 出现了异常， KeyError
# 那 data.get('key') 为什么不会报错呢？哦， 原来 data.get('Ray') 因为没有找到这个key 返回了None对象

# 所以，当我们在使用字典取值的时候，推荐大家用get的方式来获取对应的key value， 来减少try： except Exception 的使用

# 那么问题来了？ 我们怎么知道字典中有哪些key？？
# 首先 dict ， 是一个iterable的对象。


# print(data['name'], data.get('name'))

name = data.get('name')
data['name'] = '胖儿'
data.update(dict(name="Waker"))

file = open('data/demo.json', 'r')    # r  rb 对这个文件进行二进制的读取 w  wb
# json to dict or dict to json


# json.dumps()   将字典类型 转换为字符串
# {1: 2, 3: 4, 5: 6}  == >  '{"1": 2, "3": 4, "5": 6}'

_dict = {1: 2, 3: 4, 5: 6}
print(isinstance(_dict, dict))

_json = json.dumps(_dict)   # str
print(isinstance(_json, str))

# json.loads()   将字符串类型  转换为字典

# {"key": "value"}

# _new_dict = json.loads(_json)   # dict
# print(isinstance(_new_dict, dict))

# print("_new_dict", _new_dict)       # hash 实现  py3.6 字典也变为有序了
# print("_new_dict_json", json.dumps(_new_dict, sort_keys=True))


# str(dict) json.loads(dict), aes md5 dict 有序的。dumps之后的json

# json 字符串类型
# dict 类型

# with open('data/demo.json', 'r') as file:
#     data = json.loads(file.read())

# 我们如何修改这个字典中的数据呢？
"""dict中的关键字有哪些呢？
1: get
2:update
# python3.6 前， python中的dict 是无序的。
"""

# 当我们需要遍历一个字典的时候， 应该怎么做呢？好吧 这里先不讲 哈哈哈！
# 数组

# _list[0, 1, 2, 3]
_list = [1, 3, 5, "Ray", "早上", "刷牙", "Ray"]    # list是有序的，刚才我们提到的dict 其实是无序的
_list.append('狗子')
print("_list", _list)
# print(dir(_list))       # dir 查看对象包含的方法有哪些
print(len(_list), _list.__len__())
print(_list[7])
print(_list.index('Ray'))
print(_list.index('刷牙'))
# print("None", _list.index('Raymond'))
print(_list[0], _list[5])
print(_list[0], _list[7])
print(len(_list))
print("list[1]", _list[1])
print("list[3]", _list[3])
print(_list.index("早上"))
new_list = _list.copy()
name = _list.pop()
print("name", name)
print(_list.pop())
print("pop list", _list)
# print("new_list == _list", new_list == _list)
# _list.reverse()
# print(_list)

# # zip()
# # len chr ord sum

# # for list_param, new_list_param in zip(_list, new_list):
# #     print(list_param, new_list_param)

# # 变量名， 小写 + _下划线区分 + _
# # pylint/ flake8 / pycharm 自带pep8 代码静态检查工具
# # 为了符合python语言的开发标准。

print(_list)
print(new_list)
name = _list.pop()
print("name", name)
print(_list)
print(_list.pop())
print(_list)
print(_list.pop())
print(_list)

print(dir(_list))


def find_index(param, _list):
    """ 查找一个list中的元素的第一个位置 """
    for index, item in enumerate(_list):
        if item == param:
            return index

print(find_index("早上", _list))


print(_list)
print(len(_list))
print(dir(_list))

_list.append('胖儿')
_list.append(3)
_list.append(3)
_list.append(3)
_list.append('狗子')

print(_list)
print(len(_list))

print(_list.count(3))


# dict :  key , value
# list : index

for index, item in enumerate(_list):
    print(index, item)

# 我们如何解析一个list钟的
# true = True
# flase = False

"""
0 默认代表false， None [] '' {}
1 默认代表True, 非空类型的元素， 会默认为True
"""
# print(1 == 1)
# print(1 == True)
# print(0 == True)
# print(bool('') == False)

# num = 0
# while '1':
#     num += 1
#     print(num)
#     if num == 10:
#         break

# _dict = {"key": "value"}
# _list = [1, 1, 1, 1, 1, 3, 4, 3, 4, 4, 5, 6, 7, 8, 9, 0]
# print(list(set(_list)))
