#!/usr/bin/python
# -*- coding: utf-8 -*-

# 全局变量

num = 4


def change_num1():
    num = 5

def change_num2():
    global num
    num = 5

change_num1()
print(num)
change_num2()
print(num)