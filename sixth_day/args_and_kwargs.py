
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-15 06:02:34
# @FileName:  args_and_kwargs.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-15 09:00:19
"""
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


def calculator(*args, sep='+'):
    """ 20170415 计算器作业题 """
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]

    if sep == '+':
        tmp = sum([item for item in args])

    tmp = args[0]
    for index in range(len(args)):
        if args[index] == args[0]:
            continue
        if sep == '*':
            tmp *= args[index]
        if sep == '-':
            tmp -= args[index]
        if sep == '/':
            tmp /= args[index]

    if tmp >= 100000:
        raise IOError('number > 100000, calculator error !!!')
    return tmp

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
    print(calculator(100, 20, 25, sep='*'))
