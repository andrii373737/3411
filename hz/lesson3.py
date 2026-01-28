class Human:
    def __init__(self, name = 'Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def show_passengers(self):
        if self.passengers != []:
            print(f"Name of {self.brand}")
            for human in self.passengers:
                print(f"\t{human.name}")
        else:
            print(f'No passengers')


first_human = Human('Petro')
second_human = Human('Petruchenko')
car = Auto('Shkoda')
car.add_passengers(first_human)
car.add_passengers(second_human)
car.show_passengers()






