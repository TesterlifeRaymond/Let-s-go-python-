
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-15 06:02:55
# @FileName:  construction.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-15 07:00:19
"""
import random
import string
from requests import Session


def mobile():
    """ construction a new mobile """
    section_number = [130, 131, 132, 133, 135, 137, 139, 140, 155, 170, 188]
    return str(random.sample(section_number, 1)[0]) + str(random.randint(10000000, 99999999))


def email():
    """ construction a new email """
    buffer = ["163", "qq", "gmail", "yahoo"]
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, 8)) + '@' + random.sample(buffer, 1)[0] + '.com'


def name(first=None):
    """ construction a new user name """
    if first is None:
        first_name = (
            "赵钱孙李周吴郑王冯陈褚卫蒋帖沈铁伐韩铁木杨廷仝朱同秦土尤许吐万何拓略吕庹施妥张脱孔拓跋"
            "曹瓦严完华宛金完颜魏位陶委姜惟戚嵬名谢问邹瓮喻我柏吾水仵窦五章午云忤兀苏屋潘五鹿葛析奚袭范喜彭郎悉"
            "鲁西韦息昌律马隰苗凤花县方羡俞鲜"
        )
    else:
        first_name = first
    last_name = (
        "昔度黑偶呼前虎回翦咎塞矫京敛泷敬衅邝圣鲍御费夫贺仆汤镇湛藩曲邸戎府瞿戏逮凭莲进欧笃阿仁"
        "阿单仍鸡九肖圭谌徭芦蛮耒汗孛乾罕洋钼郸郯茼邗哀剑安国昂蒿奥桐傲锁机把铎斛箕磨弭浑势"
        "止己泣卷蹉赧说错夙表聊拜摆巴林办不无邦书宝保豹卑北北宫奔本闭比匕学碧鲁愚彩雪才霜财"
        "少苍梧板仓斐藏独操诗善漕祈策厕奇茶佛陀素长隐酒塔琦始天波碧镜察虿产镡禅畅澄潭謇奈风"
        "濯藤枝检驹骑貊肥雀禽飞节帛盈普建营望希载漫犁力"
    )
    rand = 1 if random.randint(0, 100) > 50 else 2
    return ''.join(random.sample(first_name, 1) + random.sample(last_name, rand))


def constuction(mobile, email):
    """ constuction request data"""
    _dict = dict()
    _dict['mobile'] = mobile
    _dict['email'] = email
    _dict['token'] = '123456'
    _dict['dealno'] = 'XFGAS12345'
    return _dict


def request(url, data):
    """ get request session """
    session = Session()
    return session, session.get(url, params=data)


if __name__ == '__main__':
    mobile, email = mobile(), email()
    print(name(['宇文', '南宫', '尉迟', '独孤']))
    # print(request('http://testerlife.com', constuction(mobile, email))[0])
