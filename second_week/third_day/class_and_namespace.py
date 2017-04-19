
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-19 06:05:06
# @FileName:  class_and_namespace.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-19 09:25:10
"""


class MyClass:
    """ my class """
    pass


class Student:
    """ pass """
    def __init__(self, name, score):
        """ pass """
        self.__name = name
        self.__score = score

    def print_score(self):
        """ pass"""
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        """ pass"""
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class StaticDemo:
    """ pass"""

    @staticmethod
    def simple():
        """pass """
        print('this is StaticDemo Class simple : )')


class ClassMethodDemo:
    """ pass """

    @classmethod
    def simple(cls):
        """ pass """
        print('this is Class MethodDemo class simple : )')


class NewStudent:
    """ the new student class """
    def __init__(self, name, age):
        """ 该init方法为类方法中的构造函数，在实例化类的时候将在此方法下定义的类属性进行初始化"""
        self.name = name
        self.age = age

    def print_score(self):
        """ pass """
        print('NewStudent"s function %s: %s' % (self.name, self.age))

new_student = NewStudent('狗子', '5')
# print(NewStudent)
# print(new_student.name, new_student.age)


def print_name_and_age(std):
    """ pass """
    print('%s: %s' % (std.name, std.age))


def scope_test():
    """# pass"""
    def do_local():
        """# pass"""
        spam = "local spam"

    def do_nonlocal():
        # pass
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        """# pass"""
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)

# if __name__ == '__main__':
#     # new_student.print_score()
#     # bart = Student('Bart Simpson', 59)
#     # bart.__score = 98
#     # print(bart.__score)
#     # print(print_name_and_age(new_student))
#     # lisa = Student('Lisa Simpson', 87)

#     # print('bart.name =', bart.name)
#     # print('bart.score =', bart.score)
#     # bart.print_score()

#     # print('grade of Bart:', bart.get_grade())
#     # print('grade of Lisa:', lisa.get_grade())
#     # StaticDemo.simple()
#     # ClassMethodDemo.simple()
