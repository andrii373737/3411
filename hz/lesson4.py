from random import randint
randint(1, 100)
class House:
    def __init__(self):
        self.food = 50
        self.mess = 100
class Human:
    def __init__(self, name = "Human"):
        self.name = name
        self.happiness = 100
        self.money = 200
        self.satiety = 70
        self.house = House()
    def relax(self):
        self.happiness += 10
        self.house.mess -= 10
    def clean_home(self):
        self.happiness -= 5
        self.house.mess += 15
    def eat(self):
        self.house.food -= 10
        self.satiety += 20
        self.happiness += 5
    def shop(self):
        self.house.food += 50
        self.money -= 100
    def do_action(self):
        dice = randint(0, 1)
        if self.happiness > 50 & dice == 0:
            self.clean_home()
        else:
            self.relax()
    def live_day(self, day):
        print(f'День: {day}')
        print(f'{self.name} - {self.happiness} - {self.satiety} - {self.money}')
        self.do_action()

first_human = Human('Petro')
for day in range(1, 8):
    first_human.live_day(day)





