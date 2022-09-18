# -*- coding: UTF-8 -*-
import time


def time1():
    s1 = range(999999999**2)
    print(id(s1))
    t1 = time.time()
    calc1 = len(s1)
    t2 = time.time()
    print(t2 - t1)


time1()


def time2():
    s2 = range(999999999**2)
    print(id(s2))
    t3 = time.time()
    calc2 = s2.__len__()
    t4 = time.time()
    print(t4 - t3)


time2()
