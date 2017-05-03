
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-03 06:14:47
# @FileName:  dailytalk.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-03 10:11:19
"""
import gevent
from requests import Session
from bs4 import BeautifulSoup


class PythonTab:
    """ spider class """
    session = Session()
    shuma_page = session.get(url='http://www.pythontab.com/')

    def page_element(self):
        """ pass """
        nav_tag = BeautifulSoup(self.shuma_page.text, 'lxml').findAll('div', {'class': 'nav-bar'})
        __result = []
        for item in nav_tag:
            for item in item.find_all('a'):
                __result.append(item.get('href'))
        return __result

    def request_nav_bar_tag(self, url):
        """ pass """
        element = BeautifulSoup(self.session.get(url).text, 'lxml')
        response = self.session.get(url).text
        title = BeautifulSoup(response, 'lxml').find('h1').get_text()
        print(title)
        for item in element.find_all('div', {'class': 'content'}):
            for item in item.find_all('p'):
                print(item.get_text())

    def daily_talk(self):
        """ 获取每日一讲页面的全部内容 class=list"""
        url = 'http://www.pythontab.com/html/hanshu/'
        response = self.session.get(url).text
        element = BeautifulSoup(response, 'lxml')
        __result = []
        for item in element.find_all('li'):
            if item.a:
                if item.a.get('href').startswith('http'):
                    __result.append(item.a.get('href'))
        return __result

if __name__ == '__main__':
    python = PythonTab()
    # print(python.daily_talk())
    # python.request_nav_bar_tag('http://www.pythontab.com/html/2013/hanshu_0216/226.html')
    events = [
        gevent.spawn(python.request_nav_bar_tag, item) for item in python.daily_talk()
    ]
    gevent.joinall(events)
