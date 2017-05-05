
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-02 05:56:12
# @FileName:  douban_books_spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-06 06:30:52
"""
import os
import json
from requests import Session
from lxml import etree


class DouBanApi:
    """ get douban books api """

    def __init__(self, book_name):
        """ pass """
        self.session = Session()
        self.book_name = book_name
        self.book_info = ''
        self.base_url = 'https://api.douban.com/v2/book/search?q={}'
        self.img = ''

    def get_book_info(self):
        """ get douban books info """
        url = self.base_url.format(self.book_name)
        self.response = self.session.get(url).json()
        self.img = self.response.get('books')

    def get_book_info_for_bookid(self, id):
        """ pass """
        print(
            self.session.get(
                'https://api.douban.com/v2/book/{}'.format(id)).json().get('translator')
        )

    def get_all_sohu_bookslist_info(self):
        """ pass """
        return os.listdir('file/')

    def down_book_info(self):
        """ pass """
        with open('file/' + self.book_name, 'w') as file:
            file.write(json.dumps(self.response))

    def get_books_name(self):
        """ pass """
        url = 'http://www.bbtpress.com/homepagebook/tsjt.asp'
        response = self.session.get(url)
        response.encoding = 'gb2312'
        source = etree.HTML(response.text).xpath('//a[@class="blacklink"]/text()')
        for item in source:
            with open('file/' + item, 'a') as file:
                file.write('')


if __name__ == '__main__':
    fammer = DouBanApi('农夫与蛇')
    fammer.get_book_info()

    xiaohongmao = DouBanApi('小红帽')
    # xiaohongmao.get_book_info()
    xiaohongmao.get_all_sohu_bookslist_info()
    # xiaohongmao.download_book_img()
    # xiaohongmao.get_books_name()

    for item in xiaohongmao.get_all_sohu_bookslist_info():
        search = DouBanApi(item)
        search.get_book_info()
        search.down_book_info()
