
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-04 06:09:18
# @FileName:  pythontab.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-04 07:45:06
"""
import gevent
from requests import Session
from bs4 import BeautifulSoup
from lxml import etree


class PythonTab:
    """ Python tab class """
    session = Session()
    homepage = 'http://www.pythontab.com/'
    tags = {}

    def get_page_nav_tag(self):
        """ home page nav """
        source = self.session.get(self.homepage).text
        element = BeautifulSoup(source, 'lxml').find_all('ul', {'class': 'nav-site'})
        for item in element:
            for _item in item.find_all('a'):
                self.tags.update({_item.get_text().split()[0]: _item.get('href')})
        return self

    def python_basic_course(self, title):
        """ Basic course """
        url = self.get_page_nav_tag().tags.get(title)
        if url:
            return url
        return

    def get_pages_number(self):
        """ page numbers """
        param = 'Python基础教程'
        source = etree.HTML(self.session.get(self.python_basic_course(param)).text)
        lase_page_number = source.xpath('//div[@class="text-c"]/a/text()')[-2]
        return lase_page_number

    def request_nav_bar_tag(self, url):
        """ pass """
        element = BeautifulSoup(self.session.get(url).text, 'lxml')
        response = self.session.get(url).text
        try:
            title = BeautifulSoup(response, 'lxml').find('h1').get_text()
            print(title)
        except AttributeError:
            pass
        for item in element.find_all('div', {'class': 'content'}):
            for item in item.find_all('p'):
                print(item.get_text())

    def get_all_pages_param(self, url):
        """ pass """
        source = etree.HTML(self.session.get(url).text)
        element = source.xpath('//div[@class="col-left"]/ul/li/a/@href')
        urls = [item for item in element]
        return urls

if __name__ == '__main__':
    pythontab = PythonTab()
    page_url = []
    pages = []
    base_url = 'http://www.pythontab.com/html/pythonjichu/{}.html'
    urls = [base_url.format('index') if num == 1 else base_url.format(num) for num in range(1, 26)]
    # 基础教程全部页面的urls
    events = [gevent.spawn(pythontab.get_all_pages_param, url) for url in urls]
    # 放入gevent.spawn
    page_url += gevent.joinall(events)
    # 协程执行  获取到全部页面中的文章url
    for url in page_url:
        pages += url.value
    # pages 是所有文章的urls的list集合
    events = [gevent.spawn(pythontab.request_nav_bar_tag, url) for url in pages]
    gevent.joinall(events)
