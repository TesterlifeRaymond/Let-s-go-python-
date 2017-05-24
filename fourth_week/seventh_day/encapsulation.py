
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-07 06:03:37
# @FileName:  encapsulation.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-07 07:05:08
"""
import gevent
from requests import Session
from lxml import etree


class Base:
    """ 父类 """
    def __init__(self, encode=None):
        """ init """
        self.session = Session()
        self.encode = encode

    def request(self, url):
        """ request active """
        response = self.session.get(url)
        response.encoding = self.encode
        return response.text

    def parse(self, url, path):
        """ parse page element """
        source = etree.HTML(self.request(url))
        parse_html = source.xpath(path)
        if parse_html:
            return parse_html
        return None


class LaoShe(Base):
    """ 继承Base类 """
    def __init__(self):
        """ init class """
        Base.__init__(self)
        self.start_url = 'http://www.readers365.com/laoshewenji/lzdz/index.html'
        self.base_url = 'http://www.readers365.com/laoshewenji/lzdz/'
        self.testerhome_url = 'https://testerhome.com/topics/{}'

    def get_all_urls(self):
        """ pass """
        return self.parse(self.start_url, '//a/@href')[4:-3]

    def get_pages_text(self, url):
        """ pass """
        try:
            result = self.parse(self.testerhome_url.format(url), '//h1/text()')[0]
            print(''.join(result))
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    laoshe = LaoShe()
    events = [gevent.spawn(laoshe.get_pages_text, url) for url in range(1, 10000)]
    gevent.joinall(events)
