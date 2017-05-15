
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-05-15 06:02:55
# @FileName:  construction.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-05-16 06:47:05
"""
import random
import string
from requests import Session
import json
from jsonschema import validate


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


def constuction(user_mobile, user_email):
    """ constuction request data"""
    _dict = dict()
    _dict['mobile'] = user_mobile
    _dict['email'] = user_email
    _dict['token'] = '123456'
    _dict['dealno'] = 'XFGAS12345'
    return _dict


def request(url, data):
    """ get request session """
    session = Session()
    return session, session.get(url, params=data)


def valid_json(myjson, schname):
    """ 按照jsonSchema格式校验jsonkey、jsonkeyType、jsonCount """
    schfile = 'schema/%s' % (schname)
    with open(schfile, 'r') as f:
        mysch = json.load(f)
    try:
        validate(myjson, mysch)
    except Exception as e:
        return e
    else:
        return True
    finally:
        pass


def string2dict(data):
    """
    __GetZoneResult_ = {
    mts:'1585078',
    province:'江苏',
    catName:'中国移动',
    telString:'15850781443',
    areaVid:'30511',
    ispVid:'3236139',
    carrier:'江苏移动'
    }
    to == > json
    """
    result = []
    for item in data.split():
        if item[0] == '{':
            pass
        else:
            result.append((item.split(':')[0], item.split(':')[1][1:-2]))
    return result

if __name__ == '__main__':
    mobile, email = mobile(), email()
    print(name(['宇文', '南宫', '尉迟', '独孤']))
    # print(request('http://testerlife.com', constuction(mobile, email))[0])
