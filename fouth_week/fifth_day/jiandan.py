
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-05 06:33:36
# @FileName:  jiandan.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-05 07:57:09
"""
import gevent
from requests import Session
from lxml import etree


class JianDan:
    """ jiandan duanzi spider """

    session = Session()
    home_page = session.get('http://jandan.net/duan').text
    page_nums = eval(
        etree.HTML(home_page).xpath('//span[@class="current-comment-page"]/text()')[0]
    )[0]

    def request(self, url):
        """ pass """
        return etree.HTML(self.session.get(url).text)

    def get_all_textid(self, url):
        """ pass """
        source = self.request(url)
        tid = source.xpath('//div[@class="text"]/span/a/text()')
        tids = ["vote-" + item for item in tid]
        return tids

    def parse_page(self, url):
        """ pass """
        source = self.request(url)
        oids = self.get_all_textid(url)
        text_id = ["comment-" + item.split('-')[1] for item in oids]

        for oid, tid in zip(oids, text_id):
            text = source.xpath(
                '//li[@id="{}"]/div[1]/div[@class="row"]/div[@class="text"]'.format(tid))[0]
            text = text.xpath('string(.)').split(tid.split('-')[-1])[-1]

            vote = source.xpath('//div[@id="{}"]/span/text()'.format(oid))
            user = source.xpath(
                '//li[@id="{}"]/div[1]/div[@class="row"]/div[@class="author"]/small/a'.format(tid)
            )[0]
            name = user.items()[2][1].split('>')[-2].split('<')[0]
            oo, xx = vote

            print("**************{}**************".format(name))
            print("******************OO:{}**XX{}*".format(oo, xx))
            print(text)
            print("******************************")

if __name__ == '__main__':
    JianDan().parse_page('http://jandan.net/duan/page-2115#comments')
