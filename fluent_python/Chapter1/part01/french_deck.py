import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 定义一张牌
beer_card = Card(rank='7', suit='diamonds')
print(beer_card)

# 查看牌列表
deck = FrenchDeck()
print(deck._cards)

# 查看多少张牌
print(len(deck))

# 抽取特定的一张
print(deck[0])
print(deck[-1])

# 随机取出一张
print(choice(deck))
print(choice(deck))

# 因为实现了__contains__方法，in运算符就可以作用域这个类上，deck它是可对待对象
print(Card('Q', 'hearts') in deck)

"""
首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它们。
也就是说没有 my_object.__len__() 这种写法， 而应该使用 len(my_object)。

很多时候，特殊方法的调用是隐式的，
比如 for i in x: 这个语句， 
背后其实用的是 iter(x)，
而这个函数的背后则是 x.__iter__() 方法。
当然前提是这个方法在 x 中被实现了。

通过内置的函数(例如 len、iter、str，等等)来使用特殊方法是最好的选择。
这些内置函数不仅会调用特殊方法，通常还提供额外的好处，而且对于内置的类来说，它们的速度更快。
"""

