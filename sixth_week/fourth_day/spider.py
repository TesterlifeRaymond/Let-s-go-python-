
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-18 06:17:11
# @FileName:  spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-18 07:20:37
"""
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
        return response.text

    def parser(self, html, xpath):
        """ parser pages source """
        source = etree.HTML(html)
        return source.xpath(xpath)

    def download_img(self, content, filename):
        """ download img function """
        with open(self.img_path + filename + '.jpg', 'wb') as file:
            file.write(content.encode())


class Spider(BaseClass):
    """ pass """

    def __init__(self):
        """ pass """
        BaseClass.__init__(self)
        self.home_page = 'http://www.mmjpg.com'

    def get_pages_number(self):
        """ pass """
        last_page_num = self.parser(
            self.request(self.home_page),
            '//div[@class="page"]/a/@href')[-1]
        return last_page_num.split('/')[-1]

    def get_all_img_url(self, pages_num):
        """ pass """
        result = []
        url = "http://www.mmjpg.com/home/{}"
        for num in range(1, pages_num + 1):
            #   遍历所有页面的html
            new_url = url.format(num)
            result.append(item for item in self.parser(self.request(new_url), '//li/a/@href'))
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
        url = self.parser(self.request(url), '//div[@class="content"]/a/img/@src')[-1]
        content = self.request(url)
        self.download_img(content, url.split('/')[-2])

if __name__ == '__main__':
    spider = Spider()
    # spawn = []
    # for item in spider.get_all_img_url(int(spider.get_pages_number())):
    #     spawn.append(item.__next__())

    # events = [
    #     gevent.spawn(spider.get_img_all_pages_second_depth, spider.request(url)) for url in spawn
    # ]
    # all_urls = []
    # for item in gevent.joinall(events):
    #     for item in spider.get_img_all_urls_second_depth(item.value):
    #         all_urls.append(item)
    spider.get_img_pages_and_download('http://www.mmjpg.com/mm/12/9')
