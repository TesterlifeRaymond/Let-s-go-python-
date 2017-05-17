
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-16 06:16:17
# @FileName:  test_user_mobile.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-16 07:24:37
"""
import json
import unittest
from construction import mobile, request, valid_json, string2dict


class TestUserMobile(unittest.TestCase):
    """ test user mobile """

    def setUp(self):
        """ setUp function """
        self.mobile = mobile()
        self.url = ('http://tcc.taobao.com/cc/json/'
                    'mobile_tel_segment.htm?tel={}'.format(self.mobile))
        self.k780_url = (
            'http://api.k780.com:88/?app=phone.get&phone={}'
            '&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'.format(self.mobile))

    def test_request_api(self):
        """ request api and get response """
        data = request(self.url, None)[1].text.split('=')[1].replace('\r\n', '')
        result = dict(string2dict(data))
        with open('test.json', 'w') as file:
            file.write(json.dumps(result))
        self.assertEqual(result.get('telString'), self.mobile)
        self.assertEqual(valid_json(result, "user_mobile_jsonschema.json"), True)

    def test_request_k780_api(self):
        """ get api data and assert response """
        result = request(self.k780_url, None)[1].json()
        self.assertEqual(valid_json(result, 'k780_mobile_jsonschema.json'), True)
        self.assertEqual(result.get('result').get('phone'), self.mobile)
        self.assertEqual(result.get('result').get('par'), self.mobile[0:-4])

if __name__ == '__main__':
    unittest.main()
