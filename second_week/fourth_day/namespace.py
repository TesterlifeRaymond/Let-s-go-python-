
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-20 06:05:44
# @FileName:  namespace.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-20 06:51:08
"""


class MyClass:
    """ my class simple """
    interger = 12345

    def function(self):
        """ my class function """
        return "hello my class !, {}".format(self.interger)


class Student:
    """ my python class """

    def __init__(self, name, age, like):
        """ __init__ function """
        self.name, self.age, self.like = name, age, like

    def eat(self):
        """ some one eat """
        print('{} 正在吃蛋挞...'.format(self.name))

    def drink(self):
        """ some one drink"""
        print('{} 正在喝果汁...'.format(self.name))

    def get_age(self):
        """ pass """
        print('{} 今年 {} 岁了呢...'.format(self.name, self.age))

    def user_like(self):
        """ pass """
        print('{} 喜欢 {}'.format(self.name, self.like))


class Animal:
    """ pass """
    def run(self):
        """ animal is running """
        print("animal is running ....")


class Snake(Animal):
    """ pass """
    pass


class Dog(Animal):
    """ dog class """
    def run(self):
        """dog is running"""
        print("dog is running ....")


class Cat(Animal):
    """ cat class """
    def run(self):
        """ cat is running """
        print("cat is running ....")

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    dog = Student('狗子', '20', '看电视')
    waker = Student('Waker', '25', '泡妞')
    dog.eat()
    dog.get_age()
    dog.user_like()

    waker.eat()
    waker.drink()
    waker.user_like()
    waker.get_age()

    waker_eat = waker.eat

    x = MyClass()
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter * 2
        # 2, 4, 8, 16
    print(x.counter)
    del x.counter

    MyClass.interger = 7890
    my_class = MyClass()
    print(MyClass.function(my_class))
    print(MyClass().function())
    print(MyClass.function(MyClass()))
    print(MyClass.interger)
    print(MyClass.__doc__)
