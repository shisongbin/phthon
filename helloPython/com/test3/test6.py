#!/usr/bin/python
# -*- coding: utf-8 -*-

def test6(num1, num2, type):
    num3 = 2

    # 嵌套函数 外部无法调用
    def add(add1, add2):
        return (add1 + add2) * num3

    def sub(sub1, sub2):
        return (sub1 - sub2) * num3

    if type == '1':
        return add(num1, num2)
    else:
        return sub(num1, num2)


print(test6(2, 3, '1'))


def test7(type):
    num3 = 2

    # 嵌套函数 外部无法调用
    def add(add1, add2):
        return (add1 + add2) * num3

    def sub(sub1, sub2):
        return (sub1 - sub2) * num3

    if type == '1':
        return add
    else:
        return sub


fn1 = test7('1')
print(fn1(1, 2))
