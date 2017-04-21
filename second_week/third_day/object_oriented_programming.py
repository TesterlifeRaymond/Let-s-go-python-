
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-21 06:29:10
# @FileName:  object_oriented_programming.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-21 06:57:57
"""

std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    """ pass """
    print('%s: %s' % (std['name'], std['score']))


class Student:
    """ pass """

    def __init__(self, name, score):
        """ pass"""
        self.name, self.score = name, score

    def print_score(self):
        """ pass """
        print('%s: %s' % (self.name, self.score))


class MyClass:
    """ pass """
    pass


class Dog:
    """ pass """
    def __init__(self, legs):
        """ pass """
        self.legs = legs

    def print_condition(self):
        """ pass """
        print("%s" % self.legs)

    def result(self):
        """ pass """
        if self.legs == 4:
            return"Normal"
        else:
            return"Disable"


# class MyStudent:
#     """ pass """

#     def __init__(self, name, score):
#         """ pass """
#         self.name, self.score = name, score

# student = MyStudent('狗子', '60')

if __name__ == '__main__':
    # print_score(std1)
    # print_score(std2)
    # michael = Student('Michael', 98)
    # bob = Student('Bob', 81)

    # michael.print_score()
    # bob.print_score()
    # my_class = MyClass()
    # my_class.name = 'python 小小班'
    # my_class.student_counter = 20
    # print(my_class.name)
    # print(my_class.student_counter)
    dog = Dog(4)
    dark = Dog(2)
    print(dog.result())
    dog.print_condition()
    print(dark.result())
    dark.print_condition()
