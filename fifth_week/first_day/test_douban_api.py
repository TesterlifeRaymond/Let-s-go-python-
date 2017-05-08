
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-08 06:35:33
# @FileName:  test_douban_api.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 10:16:00
"""

import requests
from unittest import TestCase, main


class DouBanApi(TestCase):
    """ pass """

    def test_douban_bookinfo(self):
        """ pass """
        api_url = 'https://api.douban.com/v2/book/1220562'
        print(requests.get(api_url, verify=False).json())

if __name__ == '__main__':
    main()
