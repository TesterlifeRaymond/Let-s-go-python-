
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-07 06:03:37
# @FileName:  encapsulation.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-26 13:50:20
"""
from requests import Session
from lxml import etree


class Base:
    """ 父类 """
    def __init__(self, encode=None):
        """ init """
        self.session = Session()
        self.encode = 'utf-8'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.baidu.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        }

    def request(self, url):
        """ request active """
        response = self.session.get(url, headers=self.headers, allow_redirects=True)
        print(response.url)
        response.encoding = self.encode
        return response.content

    def parse(self, html, path):
        """ parse page element """
        source = etree.HTML(html)
        parse_html = source.xpath(path)
        print(parse_html)
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
        self.test_url = 'https://www.baidu.com/s?ie=UTF-8&wd={}&rn=30'

    def get_all_urls(self):
        """ pass """
        return self.parse(self.start_url, '//a/@href')[4:-3]

    def get_pages_text(self, url, path):
        """ pass """
        try:
            html = self.request(self.test_url.format(url))
            result = self.parse(html, path)
            print('\n'.join(result))
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    import re
    html = LaoShe().request(LaoShe().test_url.format('自动化汽车大亨'))
    html = r_new = re.sub('<em>|</em>', '', html.decode())
    source = etree.HTML(html)
    pages_number = source.xpath('//span[@class="pc"]/text()')
    tags = source.xpath('//div[@class="result c-container "]')
    for tag in tags:
        # print(tag.xpath('h3/a/text()')[0], tag.xpath('h3/a/@href'))
        url = tag.xpath('h3/a/@href')[0]
        try:
            html = LaoShe().request(url)
            html = r_new = re.sub('<em>|</em>', '', html.decode())
            source = etree.HTML(html)
        except:
            pass
