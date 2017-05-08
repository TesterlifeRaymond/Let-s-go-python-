
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-08 06:09:30
# @FileName:  test_unittest.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-08 10:19:44
"""
import logging
import unittest
import requests


class TestUnitTest(unittest.TestCase):
    """ pass """

    def setUp(self):
        """ pass """
        # print('这是setUp被执行')
        self.number = 1
        self.session = requests.Session()
        self.api_url = 'https://api.douban.com/v2/book/1220562'

    def tearDown(self):
        """ pass """
        # print('这是tearDown被执行')
        del self.number

    def test_number(self):
        """ pass """
        print('start test test_number')
        self.assertEqual(type(self.number), int, "self.number is interger")
        self.assertNotEqual(self.number, 2)
        self.assertTrue(self.number)
        self.assertFalse(self.number - 1)
        self.assertIs(self.number, 1)
        with self.assertLogs('test', level='INFO') as log:
            logging.getLogger('test').info('first message')
            logging.getLogger('test.bar').error('second message')
            self.assertEqual(
                log.output,
                ['INFO:test:first message', 'ERROR:test.bar:second message']
            )
            logging.getLogger('test').info('third message ')

    def test_douban_api(self):
        """ pass """
        print('start test test_douban_api')
        result = self.session.get(self.api_url, verify=False).json()
        self.assertEqual(result.get('id'), '1220562')
        self.assertEquals(result.get('title'), '满月之夜白鲸现')
        self.assertEqual(type(result.get('tags')), list)
        self.assertIn('片山恭一', result.get('author')[0], 'a in b')

    @unittest.skip('pass test this func')
    def test_skip_test(self):
        """ pass """
        print('start test test_skip_test')

if __name__ == '__main__':
    unittest.main()
