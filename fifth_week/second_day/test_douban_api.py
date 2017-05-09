
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-09 06:07:58
# @FileName:  test_douban_api.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-09 08:00:45
"""
import time
from requests import Session
import unittest
import BSTestRunner

user = [
    'tabris17',
    '104562976',
    '57514530',
]


class TestDouBanApi(unittest.TestCase):
    """ test dou ban apis """

    def setUp(self):
        """ pass """
        self.api_url = 'http://api.douban.com/labs/bubbler/user/{}'
        self.session = Session()
        self.home_page = 'http://www.douban.com/people/{}'

    def test_first_user_info(self):
        """ pass """
        userid = user[0]
        result = self.session.get(self.api_url.format(userid)).json()
        self.assertEqual(result.get('id'), '1832573')
        self.assertEqual(result.get('uid'), userid)
        self.assertEqual(result.get('homepage'), self.home_page.format(userid))

    def test_second_user_info(self):
        """ pass """
        userid = user[1]
        result = self.session.get(self.api_url.format(userid)).json()
        self.assertEqual(result.get('id'), '104562976')
        self.assertEqual(result.get('uid'), userid)
        self.assertEqual(result.get('homepage'), self.home_page.format(userid))

    def test_third_user_info(self):
        """ pass """
        userid = user[2]
        result = self.session.get(self.api_url.format(userid)).json()
        self.assertEqual(result.get('id'), '57514530')
        self.assertEqual(result.get('uid'), userid)
        self.assertEqual(result.get('homepage'), self.home_page.format(userid))

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.', pattern='test_*.py')
    with open("report.html", 'wb') as files:
        runner = BSTestRunner.BSTestRunner(
            files,
            title='TestReport_{0}'.format(int(time.time())),
            description=u''
        )
        runner.run(suite)
