
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-22 06:02:06
# @FileName:  reviews_the_first_two_weeks.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-22 07:08:22
"""



class MyException(Exception):
    """ pass """
    def __init__(self, err):
        """ pass """
        Exception.__init__(self)
        self.err = err


def _sum(x_arg, y_arg):
    """ 求和函数"""
    print("x_arg", x_arg, "y_arg", y_arg)
    result = x_arg + y_arg
    return result


def search(name, age):
    """ pass """
    lists = ['狗子', 'Waker', 'Ray', 'LiLei', 'Lee']
    if name not in lists:
        try:
            raise MyException("he's not python class student !!!")
        except MyException as var:
            print("MyException : ", var.err)

        except TypeError as typ:
            print('TypeError :', typ)

        except IOError as io:
            print('IOError :', io)

        except Exception as exception:
            print(exception)

        else:
            print('Over')
        """ else：如果try里面的语句可以正常执行，那么就执行else里面的语句（相当于程序没有碰到致命性错误）"""
    return "{} age is {}".format(name, age)


def function(name, age=None):
    """ pass """
    print("{}'s age is {}".format(name, age))


def age(name, *args, **kwargs):
    """ pass """
    print(args, type(args))
    print(kwargs, type(kwargs))
    if name not in args:
        try:
            raise MyException("he's not python class student !!!")
        except MyException as var:
            print("MyException : ", var.err)

    return "{} age is {}".format(name, kwargs.get('age'))

if __name__ == '__main__':
    print(age(
        'LiLei', '狗子', 'Waker', 'Ray', 'LiLei', 'Lee',
        age=23, sex="male"
    ))

    # for number in range(10):
    #     print(_sum(number, random.randint(0, 20)))
    # print(search('Wake', 234))
    # print(search('狗子', '666'))
    # print(search('Lee', '233'))
    # print(search('Waker', '456'))
    # print(search('Max', '55'))
    # print(search('Ray', "20"))
