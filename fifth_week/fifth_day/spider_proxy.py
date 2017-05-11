
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-12 06:23:25
# @FileName:  spider_proxy.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-12 07:12:18
"""

from requests import Session
from lxml import etree


class TesterHome:
    """ pass """

    def __init__(self):
        """ pass """
        self.session = Session()
        self.url = 'https://testerhome.com/account/sign_in'
        self.username = ''
        self.password = ''
        self.request_data = {
            "utf8": "✓",
            "user[login]": "liujinjia@testerlife.com",
            "user[password]": "qwer1234",
            "user[remember_me]": 0,
            "commit": "登录"
        }
        self.headers = {
            "X-CSRF-Token": self.get_csrftoken(),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest"
        }

    def get_csrftoken(self):
        """ pass """
        page = self.session.post(self.url, self.request_data).content
        source = etree.HTML(page)
        csrf_token = source.xpath('//meta[@name="csrf-token"]')[0].values()[1]
        return csrf_token

    def request_home_page(self):
        """ pass """
        self.session.post(self.url, self.request_data, headers=self.headers)
        self.session.get('https://testerhome.com/').text


if __name__ == '__main__':
    TesterHome().request_home_page()
