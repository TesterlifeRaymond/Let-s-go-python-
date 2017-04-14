
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-14 06:01:34
# @FileName:  function_and_keywords.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-14 07:24:52
"""


def ask_ok(prompt, retries=4, complaint="Yes or no, please!"):
    """ ask ok function """
    while 1:
        #   1 可以代表True
        #   非空的字符串， 非空的字典，非空的元组和非空的数组
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True

        if ok in ('n', 'no', 'nope', 'nop'):
            return False

        retries -= 1
        if retries < 0:
            raise IOError('uncooperative user')
            #   raise 抛出异常 IOError
        print(complaint)

interger = 5


def func(arg=interger):
    """ pass """
    print(arg)


def function(number, _list=None):
    """ number append _list """
    if _list is None:       # 如果进if 则代表_list的值==None
        _list = []          # 那么我们将_list赋值为[]   None ==> []
    _list.append(number)
    return _list


def _parrot(*args, **kwargs):
    """ 如果我们不确定这个函数需要接受多少个关键字和参数的时候，我们可以使用*args, **kwargs
    的形式来接受位置的参数
    """
    print("args:", args)
    print("kwargs:", kwargs)
    # print("this porrot wouldn't", action, end=" ")
    # print("if you put", voltage, 'volts through it.')
    # print("-- Lovely plumage, the", type)
    # print("-- It's", state, "!")


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """ pass """
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def function(a):
    """pass """
    pass


def cheeseshop(kind, *args, **kwargs):
    """ pass """
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    keys = sorted(kwargs.keys())    # type(kwargs) == > dict, dict.keys()
    for kw in keys:
        print(kw, ":", kwargs[kw])  # dict[key], dict.get(key)

""" 以下内容是20170613python小小班作业答案"""

# def new_num():
#     """ get random number """
#     while 1:
#         num = random.randint(1000, 9999)
#         if len(set(list(str(num)))) is 4:
#             return num


# def guess_num(num):
#     """guess number's game """
#     print(num)
#     while 1:
#         right = error = 0
#         right_list = error_list = []
#         guess = input("please guess this num :")
#         if list(guess) == num:
#             return "success ! it's right ! "
#         for index, param in zip(num, list(guess)):
#             #   同时遍历两个相同长度的list
#             if index == param:
#                 #   比较list中相同位置的参数是否相等， 如果相等，则right变量+1
#                 right_list.append(index)
#                 right += 1
#             if param in num and param is not index:
#                 #   如果5在[5,0,7,6]这个list中，并且 5不等于index
#                 #   如果位置不对但数字正确，则error变量+1
#                 error_list.append(param)
#                 error += 1
#         print("{0}A{1}B".format(right, error))

file = open('file/log.log', 'w')


def write_multiple_items(separator, *args, file=file):
    """ write log """
    file.write(separator.join(args))


if __name__ == '__main__':
    write_multiple_items('Ray', 'Age', 'sex', 'compty', '狗子')
    file.close()
    with open('file/log.log', 'r') as file:
        data = file.read()
    print(data)

    # 作业题：
    # 1： 写一个计算器， 可以做 + - * / , 这个计算器之运算0以上的数字， 正数， 如果计算数值大于10W跑出IO异常
    # 2： 写一个函数，接受任意参数(可以是数字, 字符串，文件流)， 判断不同的参数类型，对参数进行不同的处理
    #     2.1 如果是file， 需要读取file文件中的信息并打印在控制台
    #     2.2 如果是int 判断下一个元素的类型，如果两个元素的类型都是int 则返回两个元素之和， 如果两个元素类型不相同，则返回int -1 的结果
    #     2.3 如果str 判断下一个类型是不是list，如果是list 将list转换为str ，两者相加之后返回，如果不是list则把str转换为list后返回

    # print(ask_ok('Do you really want to quit?', retries=2, complaint='Come on, only yes or no!'))
    # _parrot(
    #     'a million', '1', '2', action='bereft of life', voltage='jump',
    #     abc=456, aima="艾玛", doubi='狗子'
    # )
    # parrot('a', 'b', 'c', 'd')
    # parrot(voltage='a', state='c', type='1000')
    # function(0, a=0)
    # cheeseshop(
    #     "Limburger",
    #     "It's very runny, sir.",
    #     "It's really very, VERY runny, sir.",
    #     shopkeeper="Michael Palin",
    #     client="John Cleese",
    #     sketch="Cheese Shop Sketch"
    # )
