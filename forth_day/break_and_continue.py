
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-13 06:01:22
# @FileName:  break_and_continue.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-13 10:04:26
"""
import random

while 1:
    for item in range(10):
        print(item)     # item = 0
        break
    break
    # break 跳出最近一级的循环


_list = ["Ray", "LiLei", "HanMeiMei", "狗子", "waker"]

for item in _list:
    print(item)

print("it's over")


while 0:
    pass
else:
    print(1)

  这个数本身只能被自己和1整除

for item in range(2, 10):
    #  item start 2 , stop 9
    for _item in range(2, item):
        if item % _item == 0:
            print(item, 'equals', _item, '*', item // _item)
            break
    else:
        print(item, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        # % 取余，  // 取整  python运算符
        print("Found an even number", num)
        continue
    print("Found a number", num)

for letter in 'Python':     # 第一个实例
    if letter == 'h':
        pass    # 留空行，不做任何处理
    print('当前字母 :', letter)


class MyFirstClass:
    """ demo class """
    pass


def sum(number):
    """ return number += 1"""
    number += 1
    return number

enu = {
    "run": "狗子跑的快",
    "eat": "狗子吃的多",
    "fly": "狗子不会飞",
    "sleep": "狗子睡的香"
}


def active(current):
    """ 这是一个狗子的日常行为集合，通过不同的参数来获取狗子正在做什么 """
    return enu.get(current, "狗子不知道这是什么行为")


def _active(current="eat"):
    """ 这是一个狗子的日常行为集合，通过不同的参数来获取狗子正在做什么 """
    return enu.get(current, "狗子不知道这是什么行为")

#   python parameter 有两种， 1： 形参  2：实参


def function(*args, **kwargs):
    """ pass """
    # args = function(1, 2, 3, 4, 5)
    # kwargs = function(key=value, values=[], dict=enu)
    pass


def fib(n):
    """ fib func"""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, b + a
        continue


def func(a, b):
    """ pass """
    return a + b


def _func(a=3, b=6):
    """ pass"""
    print("a", a)
    print("b", b)
    return a + b


def random_number():
    """ get random number """
    while 1:
        number = random.randint(1000, 9999)
        if len(set(list(str(number)))) is 4:
            return number

if __name__ == '__main__':
    print(random_number())
