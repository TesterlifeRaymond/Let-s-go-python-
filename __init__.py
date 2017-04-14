
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-06 06:34:11
# @FileName:  __init__.py
# @Project: devops
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-14 18:05:31
"""


def print_args(*args):
    """print"""
    print(args)
    if isinstance(args[0], str):
        if isinstance(args[1], list):
            return args[0] + str(args[1])
        else:
            print(args[0])
            return list(args[0])

print(print_args('aaa', [1, 2, 3]))
