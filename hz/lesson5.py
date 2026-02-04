import requests

#1

def func(a, b):
    return a+b

#2

intro_list = []
print(type(func))
print(type(intro_list))

#3

for method in dir(intro_list):
    print(method)

#4

print(hasattr(intro_list,'print'))
print(hasattr(intro_list,'append'))
print(getattr(intro_list, 'reverse', None))
print(getattr(intro_list, 'r', None))

#5

res = callable(func)
print(res)
ret = callable(intro_list)
print(ret)

#6

class rP:
    pass
class r(rP):
    pass
print(issubclass(r, rP))
print(issubclass(rP, r))

#7

class rr:
    pass
obj = r()
print(isinstance(obj, r))
print(isinstance(obj, rP))
print(isinstance(obj, rr))

#8

import inspect

print(inspect.ismodule(r))
print(inspect.ismodule(rr))
print(inspect.ismodule(rP))

print(inspect.isclass(r))
print(inspect.isclass(requests))

print(inspect.isfunction(func))
print(inspect.isfunction(r))

'''print(inspect.getmodule(rP))'''

#9

class Par:
    def __init__(self, name = 'Marko', age = 91, height = 152):
        self.name = name
        self.age = age
        self.height = height

class Chi:
    pass

resilt = inspect.signature(Par)
for param in resilt.parameters.values():
    print(param.name, param.default)

#10      

import sys




