"""
@ Version : ??
@ Author  : liujinjia
@ File    : nbmock.py
@ Project : Let-s-go-python-
@ Create Time: 2017-05-23 06:18
"""
# import os
# import sys
# print(os.path.abspath('../'))   #   获取该层级上一层级路径的绝对路径
# sys.path.append(os.path.abspath('../')) #   加入到sys.path中


"""虽然这种方法有时会很有效， 但是慎用，在正式的项目中，尽量少的使用该方法
通过定义统一的source root 来编写项目， 是符合pep8规范的
"""
from ..doraemon import doraemon
print(doraemon)


class NbMock:
    """ pass """
