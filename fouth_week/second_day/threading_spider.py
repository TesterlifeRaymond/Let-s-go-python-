
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-02 17:54:01
# @FileName:  threading_spider.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-02 18:01:01
"""
import queue
import threading
import requests
import time
from bs4 import BeautifulSoup
hosts = ["http://163.com", "http://qq.com", "http://taobao.com"]

_queue = queue.Queue()
# 存放网址的队列
out_queue = queue.Queue()
# 存放网址页面的队列


class ThreadUrl(threading.Thread):
    """ pass """
    def __init__(self, queue, out_queue):
        """ pass """
        threading.Thread.__init__(self)
        self.queue = _queue
        self.out_queue = out_queue

    def run(self):
        """ pass """
        while True:
            host = self.queue.get()
            url = requests.get(host)
            chunk = url.text
            print(chunk)
            self.out_queue.put(chunk)
            # 将hosts中的页面传给out_queue
            self.queue.task_done()
            # 传入一个相当于完成一个任务


class DatamineThread(threading.Thread):
    """ pass """
    def __init__(self, out_queue):
        """ pass """
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        """ pass """
        while True:
            chunk = self.out_queue.get()
            soup = BeautifulSoup(chunk)
            # 从源代码中搜索title标签的内容
            print(soup.findAll(['title']))
            self.out_queue.task_done()

start = time.time()


def main():
    """ pass """
    for i in range(5):
        t = ThreadUrl(_queue, out_queue)
        # 线程任务就是将网址的源代码存放到out_queue队列中
        t.setDaemon(True)
        # 设置为守护线程
        t.start()

    # 将网址都存放到queue队列中
    for host in hosts:
        _queue.put(host)

    for i in range(5):
        DatamineThread(out_queue).run()
        # 线程任务就是从源代码中解析出

if __name__ == '__main__':
    main()
