
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-12 05:56:38
# @FileName:  while_if_and_for.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-12 07:40:50
"""
# switch = 1
#   如果 swich = 真  bool True
#   break 跳出循环

# while switch:
#     print('hello world')
#     break


# a, b = 0, 1
# while b < 10:
#     print(b, end=(','))
#     a, b = b, a + b

# print(3**2)
# print(4 ** 2)
# print(abs(-3))
# abs(-3)
#    abs函数是python的内置函数， 作用是取参数的绝对值，不取整

# print('"', '\'')
# print("\"", "'")

# user = int(input("please enter a interger : "))
# # 用户通过input这个函数 输入一个字符串类型的参数
# # int(string) 将他强转为int类型        string ==> interger
# if user < 0:
#     user = 0
#     print('Negative changed to zero')
# elif user == 0:
#     print('Zero')
# elif user == 1:
#     print("One")
# else:
#     print("More")

# ENU = {0: 'Zero', 1: 'One', 2: 'More', 3: 'Negative changed to zero'}
# print(ENU.get(user, 'Negative changed to zero'))

# if user == 0:
#     print('Zero')

# if user == 1:
#     print('One')

# if user < 0:
#     print('Negative changed to zero ')

# # else:
# #     print('More')

# """
# == 值相等
# is  是否为同一个对象
# != 不相等的值

# if a == 5:
#     do some thing
# else if :
#     print(2)
#     if 3:
#         print(3)
#     else if :
#         print(4)
#         if 5:
#             xxxx
# """

# # words = ['狗子', '大U', '小曾', '胖', '天歌']

# # for item in words:
# #     print(item)

# # print('******'.center(50, '*'))

# # 数据集合的列表 = words
# # for 遍历元素 in 数据集合的列表:
# #     print(遍历元素)

# words = ['cat', 'window', 'defenestrate']

# for word in words[:]:
#     if len(word) > 6:
#         words.insert(0, word)
# print(words)

#   猜数字的小游戏
#   用户输入一个数字， 程序可以写死一个4位数的int类型的数字
#   如果用户输入的数字大于写死的数字， 则提示数字过大， 请重新输入
#   如果输入小与 同上逻辑
#   如果用户猜对了， 则跳出循环

"""num = 1500
while True:
    user = int(input('please enter interger :'))
    if user == num:
        print(" yeah ! it's right !")
        break

    if user > num:
        print(" input number is larger.")

    else:
        print('input number is small.')"""

# for number in range(10):
#     print(number)

# print(list(range(10)))      # 获得一个0-9的list
# print(list(range(1, 11)))   # 1 - 10的list
# range(start, stop, step)
# start 起始点
# stop 终止点
# step 步长
# print(list(range(0, 30, 5)))

_list = ['Mary', 'had', 'a', 'little', 'lamb']

# print(len(_list))
# # range(len(_list))  == range(5) == 0 --> 4
# for item in range(len(_list)):
#     print(item, _list[item])

# for index, item in enumerate(_list):
#     print(index, item)

# #   已知有一个列表
# #   这个列表的长度 > 20
# #   我想取出这个列表中索引位置为5， 10 ，15的元素的值

table = [1, 4, 6, 8, 90, 0, 74, 4, 66, 89, 0, 64, 34, 3, 5, 78, 9, 896, 43, 3]

for item in range(5, 20, 5):
    print(table[item])
# print([item for item in range(5, 30, 5)][0:3])
print([item for index, item in enumerate(table) if index in (5, 10, 15)])

# for index, item in enumerate(table):
#     print(index, item)

# for index, item in enumerate(table):
#     if index == 5:
#         print(item)
#     if index == 10:
#         print(item)
#     if index == 15:
#         print(item)

# print(list(x for x in range(5, 30, 5))[0:3])

# 2017 04 11 作业解答
# 1：常用的换行操作 \n   """ \ """多行换行   ("text" "text")
# 2： 字符串拼接的常用方法有3种
#     2.1 ： string + string
#     2.2 : "%s 是一个中国人" % ('胖儿')
#     2.3 : "是他，是他就是他， 他的名字叫做 {}".format('小哪吒')

# 3： 字符串索引中 第一个索引是0 最后一位索引是-1
# 4: 字符串中 \ 有可能代表两种意图
#     4.1 ：字符转义 比如 print('\'')
#     4.2 :  在多行字符串换行时的结束符

# 5：对list进行去重的方法 set(list), 而获取list中某个元素出现的次数
# 可以使用list.count(param)来获取

# 6： while语句的作用是无限循环
# 7： 退出while语句可以使用break关键字来退出
