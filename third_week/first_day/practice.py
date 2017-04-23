
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-24 06:21:23
# @FileName:  practice.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-24 06:50:10
"""


class ReadFile:
    """ 这是今天的练习题中的第一题， 读取一个python文件，并对文件中的内容按照习题要求进行处理"""

    def __init__(self):
        """ 构造函数 """
        with open('file/log.log', 'r') as file:
            self.file = file.readlines()

    def get_score(self):
        """ 获取所有学生的考试成绩， 题目要求需要获取得分低于60的学生有哪些 """
        for item in self.file[0::2]:
            name = item.split(',')[0].replace('\n', '')
            score = int(item.split(',')[2].replace('\n', ''))
            if score < 60:
                print(name, score)

    def get_username_startswith_l(self):
        """ 获取这些学生中， 谁的名字是大写的L 开头 """
        for item in self.file[0::2]:
            if item.startswith('L'):
                print(item.replace('\n', ''))

    def modify_uppercase(self):
        """ 姓名的首字母需要大写，该record.txt是否符合此要求？ 如何纠正错误的地方？"""
        for item in self.file[0::2]:
            if item.lower():
                print(item.replace('\n', '').capitalize())


if __name__ == '__main__':
    read_file = ReadFile()
    # read_file.get_score()
    # read_file.get_username_startswith_l()
    read_file.modify_uppercase()
