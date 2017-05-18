
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-18 06:17:11
# @FileName:  spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-19 06:39:40
"""
import os
from requests import Session
from lxml import etree
import gevent


class BaseClass:
    """ pass """

    def __init__(self):
        """ pass """
        self.session = Session()
        self.img_path = 'img/'

    def request(self, url):
        """ request function """
        response = self.session.get(url)
        response.encoding = 'utf-8'
        return response.content

    @staticmethod
    def parser(html, xpath):
        """ parser pages source """
        source = etree.HTML(html)
        return source.xpath(xpath)

    def download_img(self, content, filename):
        """ download img function """
        filepath = self.img_path + "{}/".format(filename.split('/')[0])
        #   需要查询一下这个路径的文件夹是否存在， 如果不存在， 则make dir一个新的文件夹
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        with open(self.img_path + "{}".format(filename), 'wb') as file:
            file.write(content)


class Spider(BaseClass):
    """ pass """

    def __init__(self):
        """ pass """
        BaseClass.__init__(self)
        self.home_page = 'http://www.mmjpg.com'

    def get_pages_number(self):
        """ pass """
        last_page_num = self.parser(
            self.request(self.home_page).decode(),
            '//div[@class="page"]/a/@href')[-1]
        return last_page_num.split('/')[-1]

    def get_all_img_url(self, pages_num):
        """ pass """
        result = []
        url = "http://www.mmjpg.com/home/{}"
        for num in range(1, pages_num + 1):
            #   遍历所有页面的html
            new_url = url.format(num)
            result.append(
                item for item in self.parser(self.request(new_url).decode(), '//li/a/@href'))
        return result

    def get_img_all_pages_second_depth(self, html):
        """ get second depth """
        return self.parser(html, '//div[@class="page"]/a/@href')[-2]

    def get_img_all_urls_second_depth(self, uri):
        """ pass """
        result = []
        num = uri.split('/')[-1]
        new_uri = '/' + uri.split('/')[1] + '/' + uri.split('/')[2]
        for num in range(1, int(num) + 1):
            url = self.home_page + new_uri + '/' + str(num)
            result.append(url)
        return result

    def get_img_pages_and_download(self, url):
        """ pass """
        url = self.parser(self.request(url).decode(), '//div[@class="content"]/a/img/@src')[-1]
        content = self.request(url)
        filename = url.split('/')[-2] + '/' + url.split('/')[-1]
        self.download_img(content, filename)


def main():
    """ main function """
    spider = Spider()
    spawn = []
    for item in spider.get_all_img_url(int(spider.get_pages_number())):
        spawn.append(item.__next__())

    events = [
        gevent.spawn(spider.get_img_all_pages_second_depth, spider.request(url)) for url in spawn
    ]
    all_urls = []
    for item in gevent.joinall(events):
        for _item in spider.get_img_all_urls_second_depth(item.value):
            all_urls.append(_item)

    events = [gevent.spawn(spider.get_img_pages_and_download, url) for url in all_urls]
    gevent.joinall(events)

"""
1： 不要把所有的xpath 写在代码中， 包括以后的url地址、encoding、file path 等
2： 功能没问题的基础上， 如何调整代码的可读性
"""


if __name__ == '__main__':
    main()
