
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-08 06:35:33
# @FileName:  test_douban_api.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 10:35:27
"""
import unittest
from requests import Session


class DouBanApi(unittest.TestCase):
    """ pass """
    session = Session()
    url = 'https://api.douban.com/v2/book/1220562'

    def test_douban_bookinfo(self):
        """ pass """
        print('start test test_douban_api')
        result = self.session.get(self.url).json()
        self.assertEqual(result.get('id'), '1220562')
        self.assertEqual(result.get('title'), '满月之夜白鲸现')
        self.assertEqual(type(result.get('tags')), list)
        self.assertIn('片山恭一', result.get('author')[0], 'a in b')

if __name__ == '__main__':
    unittest.main()
