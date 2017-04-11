
"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-04-11 06:01:46
# @FileName:  string_obj.py
# @Project: Let-s-go-python-
# @Last Modified by:   Ray
# @Last Modified time: 2017-04-11 07:37:15
"""

# print(r'C:\some\name')   # C:\some\name    r''


# print("""\
# Usage: thingy [OPTIONS]\
#      -h                        Display this usage message \
#      -H hostname               Hostname to connect to\
# """)

# print("这是一本书" + "书名是鲁滨逊漂流")
# print(3 * "Ray" + "mond")
# print("abc""bcd")

text = (
    "这是一个测试信息，这条信息用来测试python"
    "换行操作后的字符串，是否显示正常"
)
# print(text)
# ['P', 'Y', 'T', 'H', 'O', 'N']
#   0 ,  1 ,  2 ,  3 ,  4,   5
#  -6   -5   -4   -3    -2   -1
# word = 'Python'
# print(word[0])      # P
# print(word[2])      # t
# print(word[5])      # n
# print(word[-1])     # n
# print(word[-3])     # h

# print(word[2:5])
# print(word[1:3])
# print(word[2::])

# print(word[:2] + word[2:])      # 包含起始的字符,不包含末尾的字符。这使得 s[:i] + s[i:] 永远等于 s
name = "Raymond"
# print(name[:4], name[4:])
# print(name[:3], name[3:])
# print(name[:2])
# print(name[4:])
# print(name[:3])

# print(name[42:])   # 一个过大的索引值(即下标值大于字符串实际长 度)将被字符串实际长度所代替,当上边界比下边界大时(即切片左值大于右值)就返回空字符串

ray = "Ray" + name[5:]
# print(ray)
# print(name)
# print("Liu" + ray[:3])
print('name\'s len: ', len(name))
print('Ray\'s len', len(ray))
print('string lenth', len('supercalifragilisticexpialidocious'))

# len的长度取决于你当前使用的python编码

print(len("中国"))

# + %s 这种形式的字符串格式化 str1 + str2 = str3
name = 'Ray'
age = '18'
text = "my name is {} , age is {}".format(name, age)
# sql = "select * from user where user.mobile = {}".format(mobile)  # pymysql
print(text)
text = "my name is %s , age is %s" % ("Liu", "22")
print(text)

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[:])   # squares的浅拷贝信息

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
# 1 8 27 64 125
print(cubes[3])     # 4 ** 3  is  64 not 65
cubes[3] = 64
print("修正后的list数据为：", cubes)
cubes.append(216)
cubes.append(7 ** 3)
cubes.append(8 ** 3)
cubes.insert(-1, 9 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

data = [[1, 2, 3], ['x', 'y', 'z'], ['a', 'b', 'c'], "a", "b"]
print("len(data) = ", len(data))
print(data[0][2])
print(data[1][1])
print(data[2][0])
