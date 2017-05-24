
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-10 06:00:38
# @FileName:  wrapper.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-22 14:07:01
"""
import time
import requests
from decorator import decorator
from functools import update_wrapper
from lxml import etree


@decorator
def wrapper(function, *args, **kwargs):
    """ 通过decorator来定义一个装饰器"""
    start = time.time()
    print('start time is {}'.format(start))
    result = function(*args, **kwargs)
    end = time.time() - start
    print('end time is {}'.format(end))
    return result


def _wrap(function):
    """ wrap functions """
    def load_time(*args, **kwargs):
        """ pass """
        start = time.time()
        print('start time is {}'.format(start))
        result = function(*args, **kwargs)
        end = time.time() - start
        print('end time is {}'.format(end))
        return result
    return update_wrapper(load_time, function)


class Wrapper:
    """ pass """
    def __init__(self, encoding=None):
        """ pass """
        if encoding is None:
            self.param = 'utf-8'
        self.param = encoding

    def __call__(self, function):
        """ pass """
        def parse(*args, **kwargs):
            """ pass """
            func = function(*args, **kwargs)
            if isinstance(func, str):
                return func
            xpath = kwargs.get('xpath')
            func.encoding = self.param
            source = etree.HTML(func.text)
            resp = source.xpath(xpath)
            return resp
        return update_wrapper(parse, function)


@Wrapper(encoding=None)
def wrap():
    """ wrap function """
    return '这是一个装饰器测试函数'


@Wrapper(encoding='utf-8')
def request(url, xpath=None):
    """ :type xpath: object """
    print(xpath)
    return requests.get(url)

if __name__ == '__main__':
    print(request('http://testerlife.com', xpath='//a[@class="article-title"]/text()'))
    # print(request('http://testerlife.com', xpath='//div[@class="article-meta"]/a/@href'))
    # print(request('http://www.readers365.com/laoshewenji/lzdz/index.html', xpath='//a/@href'))
    # text = ''.join(request(
    #     'https://testerhome.com/topics/2',
    #     xpath='//div[@class="panel-body markdown markdown-toc"]//text()')
    # )
    # print(','.join(text.split()))
    # __wrapper = wrap
    # __wrapper()
    # print(wrap.__name__)
    # print(__wrapper.__name__)
    # print(__wrapper is wrap)
    # Wrapper(wrap())
