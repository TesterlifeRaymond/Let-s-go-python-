
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-06 06:35:03
# @FileName:  laoshewenji.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-06 06:51:23
"""

from requests import Session
from lxml import etree
import gevent


class LaoShe:
    """ crawl """

    session = Session()
    url = 'http://www.readers365.com/laoshewenji/lzdz/index.html'
    text_path = '//a/text()'
    urls_path = '//a/@href'
    base_url = 'http://www.readers365.com/laoshewenji/lzdz/'

    @classmethod
    def get_page_param(cls):
        """ pass """
        page = cls.session.get(cls.url)
        page.encoding = 'gb2312'
        source = etree.HTML(page.text)
        urls = source.xpath(cls.urls_path)[4:-3]
        return urls

    @classmethod
    def get_page_text(cls, url):
        """ pass """
        page = cls.session.get(cls.base_url + url)
        page.encoding = 'gb2312'
        source = etree.HTML(page.text).xpath('//td/text()')
        print(''.join(source).replace('\r', '').replace('\t', '').replace('\n', ''))


if __name__ == '__main__':
    events = [gevent.spawn(LaoShe.get_page_text, url) for url in LaoShe.get_page_param()]
    gevent.joinall(events)
