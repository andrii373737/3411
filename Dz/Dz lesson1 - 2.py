# from random import randint
# random_number = randint(1, 10)

# x = input('Введіть ваше ім`я : ')
# y = int(input('Введіть ваш вік : '))

# print('Привіт, ', x, ', тобі ', y, ' років!')



# a = int(input('Введіть ваш вік : '))

# if a > 18:
#    print("Вхід дозволено!")
# elif a < 18:
#    print('Вхід заборонено!')


# r = random_number

# o = int(input('Вгадай число від 1 до 10 : '))

# if r == o:
#     print('Ти вгадав!')
# elif o > r:
#     print('Меньше')
# elif o < r:
#     print('Більше')

# o = int(input('Вгадай число від 1 до 10 : '))

# if r == o:
#     print('Ти вгадав!')
# elif o > r:
#     print('Меньше')
# elif o < r:
#     print('Більше')

# o = int(input('Вгадай число від 1 до 10 : '))

# if r == o:
#     print('Ти вгадав!')
# else:
#     print('Ти не вгадав')



# start = int(input("Введіть число З якого почати: "))
# end = int(input("Введіть число ПО яке виводити: "))

# print(f"Виводжу числа від {start} до {end}:")

# for i in range(start, end + 1):
#     print(i)



# n = int(input("Введіть число n: "))

# for i in range(n, 0, -1):
#     if i % 2 == 0:  
#         print(i, end=" ") 




# n = int(input("Введіть число n для обчислення факторіала: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial = factorial * i 

# print(f"Факторіал числа {n} (!{n}) дорівнює: {factorial}")





# k = int(input('Скільки у вас балів за екзамен? :'))

# if k > 89:
#     print('Відмінно')
# elif k > 69 :
#     print("Добре")
# elif k > 49:
#     print('Задовільно')
# elif k > 0:
#     print("Незадовільно")




# a = int(input('Введіть число a: '))
# b = int(input('Введіть число b: '))

# print("1 - додати, 2 - Відняти, 3 - Помножити, 4 - Ділити")
# diia = input("Оберіть номер дії: ")

# if diia == '1':
#     print(f"Результат: {a + b}")
# elif diia == '2':
#     print(f"Результат: {a - b}")
# elif diia == '3':
#     print(f"Результат: {a * b}")
# elif diia == '4':
#     if b == 0: 
#         print("Помилка! Ділення на нуль.")
#     else:
#         print(f"Результат: {a / b}")





#  #                                           DZ 2




# class BankAccount:
#     def __init__(self, account_number, balance=0):
        
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
        
#         if amount > 0:
#             self.balance += amount
#             print(f"Рахунок {self.account_number}: Поповнено на {amount}. Новий баланс: {self.balance}")
#         else:
#             print("Сума поповнення має бути більшою за нуль.")

#     def withdraw(self, amount):
        
#         if amount > self.balance:
#             print(f"Недостатньо коштів! Ваш баланс: {self.balance}")
#         elif amount <= 0:
#             print("Сума зняття має бути більшою за нуль.")
#         else:
#             self.balance -= amount
#             print(f"Рахунок {self.account_number}: Знято {amount}. Залишок: {self.balance}")

# print('Історія вашого банківського аккаунта : ')

# my_account = BankAccount("blablabla", 500)
# my_account.deposit(200)   
# my_account.withdraw(1000) 
# my_account.withdraw(300)  





class X:
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name

my_x = X
my_x.age = 13
my_x.name = 'Petro'
my_x.weight = 50

print('Привіт, мене звати', my_x.name, 'мені ', my_x.age, 'я важу ', my_x.weight)

































 



