
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-13 06:13:06
# @FileName:  wrapper_and_unittest.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-14 06:14:56
"""
import time
import unittest
from functools import update_wrapper
from requests import Session


def load_time(function):
    """ load time wrapper """
    def wrap(*args, **kwargs):
        """ 这是装饰器的函数 """
        print("function body : {}".format(function))
        print("*args body : {}".format(args[0]))
        print("**kwargs body : {}".format(kwargs))
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time() - start
        print("function name is : {}".format(function.__name__))
        print("function end time : {}".format(end))
        return result
    return update_wrapper(wrap, function)


class LeaningUnitTest(unittest.TestCase):
    """ 这是一个复习 unittest课程的class """

    @classmethod
    @load_time
    def setUpClass(cls):
        """ 每个class 在被运行的时候 第一个被调用， 只被调用一次"""
        cls.session = Session()
        print("setUpClass")

    def setUp(self):
        """ 这是unittest 每次case之前 都会调用该方法 """
        self.session = Session()
        print("setUp")

    @load_time
    def test_case_1(self):
        """ test case 1 """
        self.assertEqual(1, 1)

    def test_case_2(self):
        """ test case 2 """
        self.assertEqual(1, 2)

    def test_case_3(self):
        """ test case 3 """
        self.assertEqual(2, 2)

    @classmethod
    def tearDownClass(cls):
        """ 每个class 在运行完成所有成员之后， 最后被调用，只调用一次 """
        del cls.session

    def tearDown(self):
        """ 每个测试case 完成后被调用"""
        del self.session


if __name__ == '__main__':
    unittest.main()
