# class Human:
#     height = "?"
#
# class Student(Human):
#     height = 192
#
# class Worker(Human):
#     pass
#
# Petro = Student()
# Petrenko = Worker()
# print(f'Petro`s height : {Petro.height}')
# print(f'Petrenko`s height : {Petrenko.height}')




# class Grandparent:
#     height = 160
#     age = 70
#
# class Parent(Grandparent):
#    age = 40
#    height = Grandparent.height + 10
#
# class Child(Parent):
#     age = 13
#     height = Parent.height - 25
#     def __init__(self):
#         print(self.age)
#         print(self.height)
# marko = (f'{Child.height}, {Child.age}')
# mariko = (f'{Parent.height}, {Parent.age}')
# mario = (f'{Grandparent.height}, {Grandparent.age}')
#
# print(marko)
# print(mariko)
# print(mario)






# class Grandparent:
#     height = 160
#     age = 70
#
# class Parent(Grandparent):
#    age = 40
#    height = Grandparent.height + 10
#
# class Child(Parent):
#     def __init__(self, age, height, money):
#         self.age = age
#         self._height = height
#         self.__money = money
#
# marko = Child(16, 145, 200)
# print(marko.height)








# class Grandparent:
#     height = 160
#     age = 70
#     def about(self):
#         print('I am a Grandparent')
#     def about_myself(self):
#         print('I am a Grandparent')
#
# class Parent(Grandparent):
#    def __init__(self, age, money):
#        self.money = 100
#        self.age = 40
#
#    height = Grandparent.height + 10
#    def about_myself(self):
#        print('I am a Parent')
#
# class Child(Parent):
#     def __init__(self, age, money):
#         super().__init__(money)
#         self.age = age
#         super().about()
#         super().about_myself()






class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

first_shape = Shape('Red')
class Rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

first_rectangle = Rectangle(first_shape.color, 1090, 20)
print(first_rectangle.color, first_rectangle.height, first_rectangle.width)
print(first_rectangle.height * first_rectangle.width)














