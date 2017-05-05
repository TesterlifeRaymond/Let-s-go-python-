
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-06 06:34:11
# @FileName:  __init__.py
# @Project: devops
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-05 15:32:23
"""

from warnings import warn
warn(Warning('response iterable was set to a string.  This appears '
             'to work but means that the server will send the '
             'data to the client char, by char.  This is almost '
             'never intended behavior, use response.data to assign '
             'strings to the response object.'), stacklevel=2)