class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

dog = Dog("Рекс", 3, "Вівчарка")
cat = Cat("Рижик", 1, "Сірий")

print(dog.name, dog.age, dog.breed)
print(cat.name, cat.age, cat.color)

