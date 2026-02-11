class HelloWorld:
    def __init__(self, hello, world):
        self.hello = hello
        self.world = world

hewo = HelloWorld('Hello', 'World!')

if hewo.world == hewo.hello:
    print('no hello world(')
elif hewo.world == hewo.world:
    x = 13
    if x == 15:
        print(0/0)
    elif x == 13:
        hewo.hello = hewo.hello
    else:
        print('O')

p = 'p'
r = 'r'
i = 'i'
n = 'n'
t = 't'

list_1 = {
    p, r, i, n, t
}


print(f'{hewo.hello} {hewo.world}')






'''
'''






# def kvadrat(num, md):
#     deg = 0
#     for nm in range(md):
#         yield num**deg
#         deg += 1
#
# resu = kvadrat(2, 9999999)
# for val in resu:
#     print(val)







# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return (f'Я бла бла бла короче {work_in_memory},' f'а потім я тоь {work} ')
#     return helper
#
# helper = helper('fud')
# print(helper('fall assleep'))
# print(helper('wolk'))



def checker(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception:

            def kvadrat(num, md):
                deg = 0
                for nm in range(md):
                    yield num ** deg
                    deg += 1

            resu = kvadrat(2, 9999999)
            for val in resu:
                print(val)
        else:
            print('Все ок і тд')
        return res
    return wrapper


@checker
def clcl(a, b):
    return a + b

clcl(1, 2)