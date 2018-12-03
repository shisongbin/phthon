#!/usr/bin/python
# -*- coding: utf-8 -*-
from com.test1.hello import string as s

print(s)

complex_a = 1 + 2j
complex_a += 2 + 4j
print(complex_a)

print(type(complex_a))

print(bool(1))

print(int(2.0))

str = "\"\"";
print(str)

# 长字符串
str = """aaa
    bbbb"""
print(str)
name = "張三"
ages = 13
money = 0.3333333
str = "测试模板{0:s}年齡是{1:d}，收入是{2:.2f}这个是空格的意思{3:10d}".format(name, ages, money, 11)
print(str)

str = "qwertyuiopadfghjklzcvbnmqwertyuiopadfghjklzcvbnm"
print(len(str))
print(str[22])
print(str.find("n"))
print(str.rfind("n"))

# 函数
def isTure():
    return 1>2;

if isTure() :
    print(True)
else:
    print(False)

if isTure():
    print(1)
elif isTure():
    print(2)
else:
    print(3)

str = "及格" if isTure() else "不集合"
print(str)
