
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-02 06:29:29
# @FileName:  sohu_books_spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-02 06:38:40
"""

from requests import Session


class SoHuBooks:
    """ get sohu books page """

    def __init__(self):
        """ pass """
        self.session = Session()
        self.url = 'http://lz.book.sohu.com/Search/getDataInfo?c=0&o=4&cs=0&page=1&s=1&q=&a=0&p=0'

    def get_books_list(self):
        """ pass """
        return self.session.get(self.url).json()

    def parse_books_list(self):
        """ pass """
        data = self.get_books_list().get('data')
        for item in data:
            print(item.get('book_detail_name'))
            with open('file/{}'.format(item.get('book_detail_name')), 'a') as file:
                file.write('')


if __name__ == '__main__':
    sohu = SoHuBooks()
    sohu.parse_books_list()
