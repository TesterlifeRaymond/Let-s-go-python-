
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-02 05:56:12
# @FileName:  douban_books_spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-02 06:41:25
"""
import os
from requests import Session


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
        print(self.response)

    def download_book_img(self):
        """ pass """
        img_name = self.img.split('/')[-1]
        content = self.session.get(self.img)
        with open('img/{}'.format(img_name), 'wb') as img:
            img.write(content.content)

    def get_book_info_for_bookid(self, id):
        """ pass """
        print(
            self.session.get(
                'https://api.douban.com/v2/book/{}'.format(id)).json().get('translator')
        )

    def get_all_sohu_bookslist_info(self):
        """ pass """
        return os.listdir('file/')

if __name__ == '__main__':
    # fammer = DouBanApi('农夫与蛇')
    # fammer.get_book_info()

    xiaohongmao = DouBanApi('小红帽')
    # xiaohongmao.get_book_info()
    xiaohongmao.get_all_sohu_bookslist_info()
    # xiaohongmao.download_book_img()

    for item in xiaohongmao.get_all_sohu_bookslist_info():
        search = DouBanApi(item)
        search.get_book_info()
