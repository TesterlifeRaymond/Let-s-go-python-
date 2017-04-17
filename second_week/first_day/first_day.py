
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-17 06:03:04
# @FileName:  first_day.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-17 09:21:18
"""
# import requests
# from bs4 import BeautifulSoup
# from first_week.fifth_day.function_and_keywords import ask_ok


def fib(num):
    """ fib func """
    a, b = 0, 1
    while b < num:
        print(b)
        a, b = b, b + a
    return


def fib2(number):
    """ fib2 func """
    result = []
    a, b = 0, 1
    while b < number:
        result.append(b)
        a, b = b, a + b
    return result


s = 'Hello, world.'
print(s)
print(repr(s))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

if __name__ == '__main__':
    # print(dir(requests))
    # print(ask_ok("==>"))
    pass
