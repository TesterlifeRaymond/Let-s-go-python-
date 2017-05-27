
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-27 06:14:48
# @FileName:  learning_keywords.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-27 08:18:24
"""
from time import sleep
from requests import Session
from selenium import webdriver


class TesterHomeWebDriverTest:
    """ 用关键字方法封装testerhome的组件元素 """
    def __init__(self, url, username, password):
        """ init function """
        driver_path = '/Users/creditease/node_modules/chromedriver/lib/chromedriver/chromedriver'
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        self.url = url
        self.username = username
        self.password = password

    def login(self):
        """ login function """
        self.driver.get(self.url)
        print('login pages is open ..')
        self.driver.find_element_by_id("user_login").send_keys(self.username)
        self.driver.find_element_by_id("user_password").send_keys(self.password)
        self.driver.find_element_by_name("commit").click()
        print('click login button ..')
        sleep(3)
        self.driver.get_screenshot_as_file('testerhome_login_page.png')

    def get_recruit_pages(self, xpath):
        """ pass """
        self.driver.get('https://testerhome.com/jobs')
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.get_screenshot_as_file('get_recruit_pages.png')

    def get_readme_pages(self, xpath):
        """ pass """
        self.driver.find_element_by_xpath(xpath).click()


class Base:
    """ Base Class """
    def __init__(self):
        """ init base class """
        self.session = Session()

    def request(self, method, url, body):
        """ 请求函数 """
        if method in ['get', 'GET']:
            if body:
                return self.session.get(url, params=body)
            return self.session.get(url)
        return self.session.post(url, body)


class Request(Base):
    """ 继承base 类"""
    base = Base()

    def __init__(self):
        """ pass """
        Base.__init__(self)

    @classmethod
    def request_api(cls, method, url, body):
        """ pass """
        return cls.request(cls.base, method, url, body)


#   关键字封装

def _sum(a, b, *args):
    """ sum function """
    return a + b + sum(args)


if __name__ == '__main__':
    # print(_sum(1, 5))
    # url = 'http://op.juhe.cn/onebox/news/words'
    # body = {"key": "e53c5f18346ba5e40309fdf7574ee25b", "dtype": ""}
    # print(Request.request_api('post', url, body).json())
    url = 'https://testerhome.com/account/sign_in'
    username = 'liujinjia@testerlife.com'
    password = "qwer1234"
    tester = TesterHomeWebDriverTest(url, username, password)
    tester.login()

    xpath = (
        "/html/body[@class='page-jobs']/div[@id='main']/div[@class='row']/div"
        "[@class='col-md-9']/div[@class='topics panel panel-default']/div[@class="
        "'panel-body item-list']/div[@class='topic media topic-8844']/div"
        "[@class='infos media-body']/div[@class='title media-heading']/a")
    tester.get_recruit_pages(xpath)
