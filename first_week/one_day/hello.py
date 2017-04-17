
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-06 06:34:42
# @FileName:  hello.py
# @Project: devops
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-16 06:20:29
"""

# 首先，大家都是初学者， 所以我们尽可能的把内容的复杂度降低。

# 其次，在学习python的过程中，廖雪峰是一个不错的选择！

# 第一个程序

# print("hello world !")

# 执行这段代码
# 这是python3版本的hello world

"abc"
# 如果想把"abc" 打印出来， 则使用print函数即可
print("abc")
print('我是行者')
print('狗子怎么还没弄好')
print('狗子我要权限你')

data = "有没有发现上面的代码 再添加了# 和 之后， 变成了注释状态？"

sql = "select * from user where username = '狗子'"
sql = 'select * from user where username = \'狗子\''
'' ""
print(sql)

# 有没有发现上面的代码 再添加了# 和 """ 之后， 变成了注释状态？

# 在python中， 常用的注释方法有多种 单行注释

# 单行注释
""" 多行注释 """

"""
print 是打印函数， 用来将传递进来的参数打印在控制台中
我们可以在解释器中执行以下命令
解释器会接受每行内容，并反馈，在编辑器中（.py）文件中，并不会这样， 只有在运行文件时才会有返回结果
例如：
    "abc"
"""

# pep8 编码规范 推荐静态代码检查工具， pylint / flake8

# pythonic 按照python的规范和标准，进行编码。

# 注释后的代码将不会被运行

# 当然 大家是否还记得我某次偶然发出来的一段中文代码呢？

打印=print    # python3中，支持中文变量名
打印('欢迎和我一起学习python，我是行者，我来自地球！')

# print 函数支持多个参数传递进来并打印。
print(1, 2, 3, 4, 5, 6, "lalala")   # 多个参数传递进来是用，分割参数位置，每个,在被答应的过程中转换为空格
