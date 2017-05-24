
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-25 06:07:20
# @FileName:  login_to_douban.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-25 06:57:37
"""


from requests import Session
from user_agent import generate_navigator


class Base:
    """ base class """
    def __init__(self):
        """ pass """
        self.session = Session()
        self.session.headers = generate_navigator()

    def request(self, method, url, body):
        """ request url function """
        if method in ['get', 'GET']:
            return self.session.get(url, params=body)
        return self.session.post(url, data=body)


class LoginWrapper(Base):
    """ pass"""

    def __init__(self, function):
        """ init function """
        Base.__init__(self)
        self.function = function
        self.login_api_path = 'https://accounts.douban.com/login'
        self.login_data = {
            "source": None,
            "redir": "https://www.douban.com",
            "form_email": "liujinjia@testerlife.com",
            "form_password": "123",
            "login": "登录"
        }

    def __call__(self, **kwargs):
        """ call function """
        method, url, data = map(kwargs.get, ['method', 'url', 'data'])
        if not url or not method:
            result = self.request('get', self.login_api_path, self.login_data)
            return result.content
        result = self.request(method, url, data)
        return result.json()


class DouBan:
    """ Dou Ban Spider class """

    @LoginWrapper
    def login_douban(self, **kwargs):
        """ pass """

if __name__ == '__main__':
    body = dict(
        method="get",
        url="http://op.juhe.cn/onebox/news/words",
        data={"key": "e53c5f18346ba5e40309fdf7574ee25b", "dtype": ""}
    )
    print(DouBan.login_douban(**body))
