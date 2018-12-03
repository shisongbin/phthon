#!/usr/bin/python
# -*- coding: utf-8 -*-

def make_coffer(name=""):
    return "制作一杯咖啡:{}".format(name)


print(make_coffer())


def sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


print(sum(1.1, 1.2))


def sum2(*numbers, num1=0):
    total = 0
    for i in numbers:
        total += i
    return total * num1


print(sum2(1, 2, 3, num1=2))


def show_dict(**dict):
    return int(dict['num1']) * int(dict['num2'])


print(show_dict(num1=1, num2=2))
