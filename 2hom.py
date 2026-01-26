from datetime import datetime

class Car:
    def __init__(self, brand=None, model=None, age=0, mileage=0):
        self.brand = brand
        self.model = model
        self.age = age
        self.mileage = mileage

    def __str__(self):
        return f"{self.brand} {self.model}, {self.age} років, {self.mileage} km"

    def __del__(self):
        print("Object deleted")

    def __bool__(self):
        return self.brand != None

    def __len__(self):
        return self.mileage

    def get_age(self):
        year_now = datetime.now().year


first_car = Car("BMW", "E46", 20, 250000)
print(first_car.brand, first_car.model, first_car.age, first_car.mileage)
print(f"Моя машина {first_car.brand} {first_car.model}. Їй {first_car.age} років")
print(first_car)

second_car = Car()
print(second_car)
print(second_car.__bool__())
print(first_car.__bool__())
print(first_car.__len__())
