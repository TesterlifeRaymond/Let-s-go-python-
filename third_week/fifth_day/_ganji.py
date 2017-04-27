
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-28 06:59:27
# @FileName:  _ganji.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-28 07:16:07
"""
import requests
from bs4 import BeautifulSoup


class GanJi:
    """ pass """
    def __init__(self):
        """ pass """
        self.session = requests.Session()

    def get_page_html(self, url):
        """ pass """
        page = self.session.get(url)
        if page.encoding != 'utf-8':
            page.encoding = 'utf-8'
        return BeautifulSoup(page.text, 'lxml')

    def get_page_all_url(self, url, tag=None, kw=None):
        """ pass """
        element = self.get_page_html(url).find_all(tag)
        return [
            'http:/' + item.a.get('href') for item in element if item.a.get('href').startswith('/')
        ]

if __name__ == '__main__':
    ganji = GanJi()
    print(ganji.get_page_all_url('http://bj.ganji.com/', tag='s'))
