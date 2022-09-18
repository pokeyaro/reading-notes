# -*- coding: UTF-8 -*-
import datetime

"""
__repr__ 所返回的字符串应该准确、无歧义，并且尽可能表达出如何 用代码创建出这个被打印的对象。因此这里使用了类似调用对象构造器的表达形式。
__repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，或是在用print函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
"""

# __str__是可读的，__repr__的目标是明确的
# 例1
print(str(1) == repr(1))
print(str(1) == str('1'))
print(repr(1) == repr('1'))
print(repr(1))
print(repr('1'))

# 例2
now = datetime.datetime.now()
print(str(now))
print(repr(now))



"""
如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择， 
因为如果一个对象没有 __str__ 函数，而 Python 又需要调用它的时候，解释器会用 __repr__ 作为替代。
"""


class Foo1:
    def __init__(self):
        self.msg = 'Foo obj'

    def __repr__(self):
        return '{} repr'.format(self.msg)

    def __str__(self):
        return '{} str'.format(self.msg)


class Foo2:
    def __repr__(self):
        return 'Foo obj repr2'


print(Foo1)
print(Foo1().__repr__())
print(Foo1())

print(Foo2)
print(Foo2())
