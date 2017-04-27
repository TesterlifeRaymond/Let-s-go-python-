
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-28 06:01:54
# @FileName:  _request_spdier.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-28 06:58:44
"""

import requests
from bs4 import BeautifulSoup
# from lxml import etree


class LianJiaSpider:
    """ 链家网爬虫 """

    def __init__(self, start_url):
        """ pass """
        self.start_url = start_url
        self.session = requests.Session()
        self._get_home_page = self.session.get(self.start_url)
        # 我们可以不需要考虑cookies， 建议大家查看一下文档中的requests的使用方法

    def _parse_home_page(self):
        """ return bs4 soup element """
        response = self._get_home_page
        if response.encoding == 'ISO-8859-1':
            response.encoding = 'UTF-8'
        print(response.text)
        return BeautifulSoup(response.text, 'lxml')

    def _city_enum_list(self):
        """ get all city url """
        element = self._parse_home_page().find_all('div', {'class': 'city-enum fl'})
        return [item.a.get('href') for item in element]

    def _request_module(self, url):
        """ pass """
        request = self.session.get(url)
        if request.encoding == 'ISO-8859-1':
            request.encoding = 'UTF-8'
        return BeautifulSoup(request.text, 'lxml')

    def _parse_all_page(self, url):
        """ pass """
        element = self._request_module(url).find_all('div', {'class': 'list'})
        for item in element:
            try:
                print(item.li.a.get('data-log_value'), item.li.a.get('href'))
            except AttributeError as ab:
                del ab
                pass


if __name__ == '__main__':
    lianjia = LianJiaSpider(
        "http://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_"
        "term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x"
    )
    for url in lianjia._city_enum_list():
        lianjia._parse_all_page(url)
