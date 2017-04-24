
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-24 06:50:53
# @FileName:  basic_practice.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-24 10:08:18
"""
import time
import random


"""
问题描述

有一个列表，其中包括10个元素，例如这个列表是[1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ] ，
要求将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。最终样式是[2,3,4,5,6,7,8,9,0,1]
"""
_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
__array = _array[1::] + [_array[0]]
print(__array)


"""
问题描述

按照下面的要求实现对列表的操作：

产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
对上面的列表元素从大到小排序
"""
student_score = [random.randint(0, 100) for _ in range(0, 41)]

print(student_score)
#   其中有40个元素，每个元素是0到100的一个随机整数

avg = sum(student_score) / len(student_score)
print("avg number is {}".format(avg))
print(len([item for item in student_score if item < avg]))
#   列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数

sorted_student_score = sorted(student_score)
sorted_student_score.reverse()
print(sorted_student_score)
#   输出对上面的列表元素从大到小排序


"""
问题描述

如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比如"How are you."，
但有的时候，会在两个单词之间多打一个空格。现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
"""
string_data = (
    "If a word is a  string, the string will  have spaces  (here only discuss  English),"
    "such as 'How are you.', but sometimes, in between two words play a space. The task now is, if"
    "a string has two consecutive spaces, delete  it."
)
print(string_data.replace('  ', ' '))


"""
编写代码, 打印1-1000之内的偶数
"""
print([item for item in range(0, 1000, 2)])


"""
请使用python, 对下面的函数进行处理，

def hello(name):
    print "hello, %s" % name

在函数被调用时打印耗时详情

也可以对函数内部进行代码修改 把需要打印的信息放在代码内部和下文顺序打印
"""


def load_time(func):
    """ 这是一个装饰器函数 """
    def wrap(*args, **kwargs):
        """ wrap func """
        print("function name is {}".format(func.__name__))
        start = time.time()
        print("func call begin")
        result = func(*args, **kwargs)
        print("func call end ")
        print("timecosts {}".format(time.time() - start))
        return result
    return wrap


@load_time
def test_wrap():
    """ test wrap """
    pass

test_wrap()


"""
有一个列表：[1, 2, 3, 4…n]，n=20；请编写代码打印如下规律的输出：
1 [1*, 2, 3, 4, 5]
2 [1, 2*, 3, 4, 5]
3 [1, 2, 3*, 4, 5]
4 [2, 3, 4*, 5, 6]
5 [3, 4, 5*, 6, 7]
6 [4, 5, 6*, 7, 8]
"""
for item in range(1, 21):
    _array = list(range(1, 21))

    if item == _array[item - 1]:
        _array[item - 1] = '{}*'.format(item)
    else:
        _array[item - 1] = item
    print(_array)
