import inspect
import colorama
import sys

# аналог func
def func(a, b):
    return a + b

# аналог intro_list
intro_list = colorama

print(type(func))            # тип функції
print(type(intro_list))      # тип об'єкта (модуль)

for method in dir(intro_list):
    print(method)            # атрибути та методи colorama

print(hasattr(intro_list, 'init'))        # чи є функція init
print(hasattr(intro_list, 'something'))   # неіснуючий атрибут

print(getattr(intro_list, 'init'))         # отримання init
print(getattr(intro_list, 'something', None))  # без помилки

result = callable(func)
print(result)                # чи є func викличною

class Parent:
    def __init__(self, autoreset=False, strip=None, convert=None):
        self.autoreset = autoreset
        self.strip = strip
        self.convert = convert

result = inspect.signature(Parent)
for param in result.parameters.values():
    print(param.name, param.default)   # параметри конструктора

class Child(Parent):
    pass

print(issubclass(Parent, Child))   # перевірка наслідування
print(issubclass(Child, Parent))   # Child наслідує Parent

print(inspect.ismodule(colorama))  # чи є colorama модулем
print(inspect.isclass(colorama))   # чи є colorama класом
print(inspect.isfunction(func))    # чи є func функцією
print(inspect.getmodule(Parent))   # модуль класу Parent

print(sys.executable)   # шлях до Python
print(sys.version)      # версія Python
print(sys.platform)     # платформа
print(sys.argv)         # аргументи запуску
