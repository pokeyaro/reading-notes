# -*- coding: UTF-8 -*-
from collections.abc import Iterable
from collections.abc import Iterator

l = [1, 2, 3]
l_iter = l.__iter__()
o_iter = (i for i in l)

"""
可迭代对象
  实现了迭代器协议的对象，iterable可迭代对象，内部定义了一个__iter__方法

使用迭代器访问对象
  iterator迭代器：内部实现了__iter__方法，和__next__方法

常见的可迭代对象有：str、list、tuple、dict、set
迭代器：tuple的列表推导式

迭代器一定是可迭代对象，但可迭代对象不一定是迭代器
"""


# 列表是可迭代对象，但它不是迭代器，他没有实现__next__方法
print(isinstance(l, Iterable))
print(isinstance(l, Iterator))

print(isinstance(l_iter, Iterable))
print(isinstance(l_iter, Iterator))

print(isinstance(o_iter, Iterable))
print(isinstance(o_iter, Iterator))

print(next(l_iter), next(l_iter), next(l_iter))
