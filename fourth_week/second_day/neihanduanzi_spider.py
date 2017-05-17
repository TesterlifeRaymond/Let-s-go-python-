
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-02 05:58:05
# @FileName:  neihanduanzi_spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-02 06:53:47
"""
from requests import Session
from bs4 import BeautifulSoup


class NeiHanWu:
    """ pass """
    __session = Session()
    __url = 'http://neihanshequ.com/'

    @classmethod
    def get_neihan_page(cls):
        """ pass"""
        page = cls.__session.get(cls.__url).text
        soup = BeautifulSoup(page, 'html.parser')
        duanzi = soup.find_all('li')
        for item in duanzi:
            if item.p:
                print('***'.center(20, '*'))
                print(item.p.get_text().replace('\n', ''))
                print('***'.center(20, '*'))

if __name__ == '__main__':
    NeiHanWu.get_neihan_page()
