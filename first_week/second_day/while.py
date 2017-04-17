
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-11 07:02:49
# @FileName:  while.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-16 07:01:04
"""
# 菲波那契 子序列的程序

a, b = 0, 1
while b < 100:  # while 无限循环
    print(b)
    a, b = b, a + b
print(a, b)

# while 1 True
# while []  False
# while '' False

a = 0  # False
while a:
    print("ok")
    break


# None  # nil null
# bool  # True or False
# set   一般我们对一个list进行去重并保留顺序的时候，可以使用set来进行操作

# if result is None:
#   do some thing

_list_a = ['a', 'b', 'd', 'e']
_list_b = ['d', 'a', 'c', 'f']

_list_c = _list_a + _list_b
print(set(_list_a) & set(_list_b))
print(list(set(_list_c)))


# 1 : print函数的作用是什么？
# print函数会把参数信息打印在控制台

# 2： python中常用到的数据类型判断的方法有哪些， 他们的区别是什么？
# type, isinstance  区别是： type 返回的 是目标对象的类型， 而isinstance 返回的是bool

# 3： 字典中取值方式有哪些，他们有什么不同
# data = {'name': 'Ray', 'age': '18', 'sex': 'male'}
# data.get('name1') , data['name1']
# .get() 获取没有的key信息的时候， 返回None， data[]则抛出异常KeyError

# 4： 我们如何快速的修改一个字典中指定key的value
# dict.update(dict(key=value))

# 5: json.dumps()只能针对于dict数据，还是可以操作其他类型？
# json.dumps(list)

# 6: 如何快速的获取字典中的全部元素
# dict.items()

# 7: 如何快速获取list全部元素的数量？
# len(), list.__len__

# 8: 如何快速的查看list中的全部方法
# dir(list)
