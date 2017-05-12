
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-06 06:34:11
# @FileName:  __init__.py
# @Project: devops
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-12 18:29:39
"""

result = []


def function(num):
    """ pass """
    start = 1
    for item in range(1, num):
        start *= item
        result.append(start)
    res_num = 0
    data = list(result)
    
    for _item in map(str, data[0]):
        if _item == 0:
            res_num += 1
        break
    print(res_num)

if __name__ == '__main__':
    function(51)
