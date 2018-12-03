#!/usr/bin/python
# -*- coding: utf-8 -*-

# 生产器 可以节省内存
def test5(num):
    for i in range(10):
        yield i * num

array = test5(5)

print(array.__next__())
print(array.__next__())