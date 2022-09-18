# -*- coding: UTF-8 -*-
from collections import namedtuple

# 定义一个namedtuple类型User，包含3个属性
User = namedtuple('User', ['name', 'gender', 'age'])

# 创建一个User对象
user = User(name='Pokeya', gender='male', age=26)
user_list = User._make(['Pokeya', 'male', 21])

# 查看该对象，对象类型
print(user, type(user))

# 依然可以通过索引值访问
print(user[0])

# 通过属性访问
print(user.name)
print(user.gender)
print(user.age)

# 修改值
user = user._replace(age=30)
print(user)

# 将对象转换成字典
print(user._asdict())
