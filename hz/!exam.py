class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

cont1 = Contact('Iryna', '+380667091378', 'irynapumpum@gmail.com')
cont2 = Contact('Petro', '+380217750291', 'petroakim@gmail.com')
cont3 = Contact('Ivan', '+380913092370', 'ivankopostribanko@gmail.com')

list = [cont1.name, cont1.number, cont1.email]
list2 = [cont2.name, cont2.number, cont2.email]
list3 = [cont3.name, cont3.number, cont3.email]

print(list)
print(list2)
print(list3)
