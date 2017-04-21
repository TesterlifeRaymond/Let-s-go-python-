
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-21 06:02:10
# @FileName:  classmethod_and__init__.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-21 06:20:49
"""


class MyClass:
    """ 我的班级类"""
    count = 20  # 班级总人数
    male = 10    # class variable shared by all instances

    def __init__(self, name):
        """ 实例类"""
        self.name = name    # instance variable unique to each instance


class Dog:
    """ dog class """
    tricks = []     # 类属性，对全部实例对象共享

    def __init__(self, name):
        """实例属性， 在这里定义的属性，在不同的实例对象中，name都不相同"""
        self.name = name

    def add_tricks(self, trick):
        """ 对类变量中的tricks这个list 进行append操作，在list末尾添加传入的trick变量的值"""
        self.tricks.append(trick)


class Cat:
    """ cat class """

    def __init__(self, name):
        """ pass """
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        """ pass """
        self.tricks.append(trick)

if __name__ == '__main__':
    # gouzi = MyClass('狗子')
    # pang = MyClass('胖')
    # lilei = MyClass('李磊')
    # print(gouzi.count)
    # print(pang.male)
    # print(lilei.count, lilei.male)
    # print(gouzi.name, pang.name, lilei.name)

    # dog = Dog('狗子')
    # dog.add_tricks('roll over')

    # waker = Dog('Waker')
    # waker.add_tricks('running ...')

    # dog.add_tricks('吃饱了')
    # print(dog.tricks)

    cat = Cat('狗子')
    waker = Cat('Waker')

    waker.add_tricks('roll over ...')
    cat.add_tricks('play dead ...')

    print(waker.tricks)
    print(cat.tricks)
