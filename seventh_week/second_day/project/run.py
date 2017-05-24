"""
@ Version : ??
@ Author  : liujinjia
@ File    : run.py
@ Project : Let-s-go-python-
@ Create Time: 2017-05-23 06:14
"""
import case

gate = case.ArbitraryGate()
gate.name = 'Gate'
gate.age = '19'
gate.sex = 'male'
gate.father = 'Doraemon'


doraemon = case.Doraemon()
doraemon.name = "doraemon"
doraemon.age = "29"
doraemon.sex = "male"


if __name__ == '__main__':
    print(gate)
    print(doraemon)
