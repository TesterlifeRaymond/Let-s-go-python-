
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-15 06:02:34
# @FileName:  args_and_kwargs.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-16 07:31:08
"""
import _io
from collections import deque
import random
from math import pi


def function(*args, **kwargs):
    """ test args and kwargs function """
    print("args", args, type(args))
    print("kwargs", kwargs, type(kwargs))


def parrot(voltage, state='a stiff', action='voom', **kwargs):
    """ pass """
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


def make_incrementor(n):
    """ pass """
    # def sum(x):
    #     return x + n
    # return sum
    return lambda x: x + n


def my_function():
    """Do nothing, but document it.  No, really, it doesn't do anything.....  """
    pass


def squares():
    """ pass """
    squares = []
    for x in range(10):
        squares.append(x)
    return squares

"""作业题：
    1： 写一个计算器， 可以做 + - * / , 这个计算器之运算0以上的数字， 正数， 如果计算数值大于10W抛出IO异常
    2： 写一个函数，接受任意参数(可以是数字, 字符串，文件流)， 判断不同的参数类型，对参数进行不同的处理
        2.1 如果是file， 需要读取file文件中的信息并打印在控制台
        2.2 如果是int 判断下一个元素的类型，如果两个元素的类型都是int 则返回两个元素之和， 如果两个元素类型不相同，则返回int -1 的结果
        2.3 如果str 判断下一个类型是不是list，如果是list 将list转换为str ，两者相加之后返回，如果不是list则把str转换为list后返回
"""


def calculator(*args, sep='+'):
    """ 20170415 计算器作业题 """
    if len(args) < 2:
        return 'args lenth is too short'

    if sep not in ['+', '-', '*', '/']:
        raise TypeError("type error for sep !")

    tmp = args[0]
    for index in range(1, len(args)):
        if sep == '+':
            tmp = sum(args)
        if sep == '*':
            tmp *= args[index]
        if sep == '-':
            tmp -= args[index]
        if sep == '/':
            tmp /= args[index]

    if tmp >= 100000:
        raise IOError('number > 100000, calculator error !!!')
    return tmp


def every_type_to_function(param, *args):
    """For different types of parameters to
    determine and return the corresponding results
    """
    result = None
    if isinstance(param, _io.TextIOWrapper):
        result = param.read()
        param.close()

    if isinstance(param, int) and args:
        if isinstance(args[0], int):
            result = param + args[0]
        else:
            result = param - 1
    if isinstance(param, str) and args:
        if isinstance(args[0], list):
            result = param + ''.join(args[0])
        else:
            result = list(param)
    return result

if __name__ == '__main__':
    # function(
    #     'Ray', '狗子', '胖儿', '茶茶', '大U',
    #     active="看电影", timing="18:00", go_home='23:00'
    # )
    # print(list(range(2, 11)))   # start 2 == > 10 的list
    # args = [3, 6]
    # print(list(range(*args)))
    # data = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    # parrot(**data)
    # print(make_incrementor(10)(10))
    # func = make_incrementor(42)
    # print(func(31))
    # pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # pairs.sort(key=lambda pair: pair[1])
    # print(pairs)
    # print(dir(my_function))
    # print(my_function.__qualname__)
    # print(my_function.__name__)
    # print(my_function.__doc__)
    # queue = deque(["Eric", "John", "Michael"])
    # queue.append("Terry")
    # queue.append("狗子")
    # queue.append("宋谦")
    # print(dir(queue))
    # queue.appendleft('Ray')
    # print(queue)
    # _list = [item ** 2 for item in range(1, 11)]
    # print(_list)
    # squares = (item for item in range(10, 21))
    # print(squares.__next__())
    # print(squares.__next__())
    # print(squares.__next__())
    # print(squares.__next__())
    # print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
    # print([(x, y) for x, y in zip([1, 2, 3], [3, 1, 4]) if x != y])
    # vec = [-4, -2, 0, 2, 4]
    # print([item * 2 for item in vec])
    # print([sum(item) for item in vec])
    # _list = []
    # for item in vec:
    #     _list.append(sum(item))
    # print(_list)
    # freshfruit = [' banana', ' loganberry ', 'passion fruit ']
    # print([weapon.strip() for weapon in freshfruit])
    # print([(x, x**2) for x in range(6)])
    # vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print([num for elem in vec for num in elem])
    # print([str(round(pi, i)) for i in range(1, 6)])     # round 四舍五入
    # #  不做str  我们列表中存入的是float
    # matrix = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    # ]
    # transposed = []
    # for i in range(4):
    #     transposed_row = []
    #     for row in matrix:
    #         transposed_row.append(row[i])
    #     transposed.append(transposed_row)

    # print([[row[i] for row in matrix] for i in range(4)])
    # print(list(zip(*matrix)))
    # a, b, c = matrix
    # print(list(zip(a, b, c)))   # reduce max

    # _list = [-1, 1, 66.25, 333, 333, 1234.5]
    # # _list = [], _list.clear(), _list = _list[999:], [_list.pop() for num in range(len(_list))]
    # del _list[0]
    # print(_list)
    # del _list[2:4]
    # print(_list)
    # del _list[:]
    # print(_list)
    # del _list
    # print(_list)

    # file = open('../fifth_day/file/log.log', 'r')
    print(every_type_to_function("100", 123))
    # print(calculator(100, 2000, 25, sep='*'))
    # enu = {
    #     1: '1',
    #     2: '2',
    #     3: '3'
    # }

    # def enum(num):
    #     """ return enm value for num """
    #     return enu.get(num, 'key error')

    # print(enum(1))
    # print(enum(2))
    # print(enum(5))
