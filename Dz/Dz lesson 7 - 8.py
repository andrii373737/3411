import logging
import datetime
now = datetime.datetime.now()

# class HelloWorld:
#     def __init__(self, hello, world):
#         self.hello = hello
#         self.world = world

# hewo = HelloWorld('Hello', 'World!')

# if hewo.world == hewo.hello:
#     print('no hello world(')
# elif hewo.world == hewo.world:
#     x = 13
#     if x == 15:
#         print(0/0)
#     elif x == 13:
#         hewo.hello = hewo.hello
#     else:
#         print('O')

# p = 'p'
# r = 'r'
# i = 'i'
# n = 'n'
# t = 't'

# list_1 = {
#     p, r, i, n, t
# }


# print(f'{hewo.hello} {hewo.world}')












def kvadrat(num, md):
    deg = 0
    for nm in range(md):
        yield num**deg
        deg += 1

resu = kvadrat(3, 30)
for val in resu:
    print(val)








                                                                                    #DZ 2












logging.basicConfig(
    level=logging.INFO,
    filename = 'Readme.log',
    filemode = 'w',
    format = 'We have next logging message: %(asctime)s, %(levelname)s, %(message)s'
)

logging.info('Програма успішно запустилась!')

