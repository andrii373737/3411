


#                                                                                   DZ 1



class Product:
    def __init__(self, name, deadline, descriptions,):
        self.name = name
        self.deadline = deadline
        self.descriptions = descriptions
        self.кількість = 1
product_1 = Product(deadline=14, name='Cookie', descriptions='Very tasty and natural')

print(f'Product deadline : {product_1.deadline} years.')
print(f'Product name : {product_1.name}.')
print(f'Product descriptione : ``{product_1.descriptions}``')

class Cart:
    def __init__(self):
        self.kilkist = 1

    def do_action(self):
        self.kilkist

    def cart(self):
        print(f'{self.add}')
        print(f'{self.kilkist}')
        self.do_action()

cart1 = Cart()
x = input("(Додати / Видалити : )")
if x == 'Додати':
    cart1.kilkist += 1
elif x == 'Видалити':
    cart1.kilkist -= 1
else:
    print('Невідома команда.')

print('Products in the cart : ', cart1.kilkist)

y = input('Add more? (Yes / No) : ')
if y == 'Yes':
    s = int(input('How many? (from 1 to 5): '))
    if s == 1:
        cart1.kilkist += 1
    elif s == 2:
        cart1.kilkist += 2
    elif s == 3:
        cart1.kilkist += 3
    elif s == 4:
        cart1.kilkist += 4
    elif s == 5:
        cart1.kilkist += 5
    print('Products in the cart : ', cart1.kilkist)

y = input('Delete? (Yes / No) : ')
if y == 'Yes':
    s = int(input('How many? (from 1 to 5): '))
    if s == 1:
        cart1.kilkist -= 1
    elif s == 2:
        cart1.kilkist -= 2
    elif s == 3:
        cart1.kilkist -= 3
    elif s == 4:
        cart1.kilkist -= 4
    elif s == 5:
        cart1.kilkist -= 5
    print('Products in the cart : ', cart1.kilkist)





#                                                                                          DZ 2






    
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

first_shape = Shape('Red')
class Circle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

first_circle = Circle(first_shape.color, 1090, 20)
print(first_circle.color, first_circle.height, first_circle.width)
print(first_circle.height * first_circle.width)






                                                                                        #   DZ 3



 



class Tvarina:
    def __init__(self, fur, claws, mouth, eyes, nose):
        self.fur = fur
        self.claws = claws
        self.mouth = mouth
        self.eyes = eyes
        self.nose = nose

class Sobaka(Tvarina):
    pass

class Kit(Tvarina):
    pass