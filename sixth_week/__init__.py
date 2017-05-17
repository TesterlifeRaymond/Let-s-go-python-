
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-15 06:02:17
# @FileName:  __init__.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-17 16:22:45
"""
import random


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for index in range(len(array)):
    try:
        print(
            random.sample(array[index], 1),
            random.sample(array[index + 1], 1),
            random.sample(array[index + 2], 1)
        )
    except:
        pass
