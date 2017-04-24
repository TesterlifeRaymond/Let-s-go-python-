
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-25 06:27:31
# @FileName:  practice.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-25 07:16:23
"""

"""给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key通过字典序升序排列(注意key可能是字符串）。
例如：a={1:1,2:2,3:3}, 则输出：1,2,3
"""
print(','.join([str(item) for item in list({1: 1, 2: 2, 3: 3}.keys())]))

"""给定一个字符串a, 将a中的大写字母 转换成小写，其它字符不变，并输出。 """
rand = 'KCWKd6w0PDS7CfJ9XLakxGFosBWnVadr'
print(rand.lower())

"""给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
"""
_list = [1, 2, 3, 4, 5, 6, 7, 6, 4, 3]


def diff_list_param(_list):
    """pass"""
    return True if len(_list) == len(set(_list)) else False


""" 给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。
如L=['abc','d','efg'], 则输出abcdefg。
"""
data = [
    'K', 'C', 'W', 'K', 'd', '6', 'w', '0', 'P', 'D', 'S', '7', 'C', 'f', 'J', '9',
    'X', 'L', 'a', 'k', 'x', 'G', 'F', 'o', 's', 'B', 'W', 'n', 'V', 'a', 'd', 'r'
]
print(''.join(data).upper())

"""给你一个字符串列表L，用一行代码顺序输出L中的元素，元素之间以一个空格隔开，注意行尾不要有空格，输出单独占一行。
如L=['abc','d','efg'], 则输出abc d efg。
"""
data = ['abc', 'd', 'efg', 'abcabc', 'def', 'hhh', ' 032ab']
print(' '.join(data))


""" 给你一个只包含括号（'('、 ')'、 '{'、 '}'、 '[' 和 ']'）的字符串seq，请你判断该序列是否是合法的括号序列。合法请输出Yes，否则输出No。
例如：
seq="()", 输出Yes
seq="()[]{}", 输出Yes
seq="(]", 输出No
seq="([)]", 输出No
"""


def diff_seq(seq):
    """ pass """
    if len(list(seq)) <= 2:
        return "Yes" if seq in ['()', '[]', '{}'] else "No"

    num = 0
    _next = 2
    _result = []
    for item in range(len(list(seq))):
        if list(seq)[num: _next]:
            print(''.join(list(seq)[num: _next]))
            _result.append(''.join(list(seq)[num: _next]) in ['()', '[]', '{}'])
            num += 2
            _next += 2
    return "Yes" if len(set(_result)) == 1 and _result[0] is True else "No"

if __name__ == '__main__':
    # print(diff_list_param(_list))
    print(diff_seq('([)]'))
