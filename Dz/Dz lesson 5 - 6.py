import inspect
import colorama

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(hasattr(colorama,'print'))
print(hasattr(colorama,'Cursor'))
print(getattr(colorama, 'reverse', None))
print(getattr(colorama, 'Back', None))
print(dir(colorama))



                                                                                    #DZ 2


try:
    print('Лист відвідувачів: Marko three, Oleg seven, Petro four')
    x = input('Your age and name (Marko three): ')

    if x == 'Marko three':
        print('Вхід дозволено!')
    elif x == 'Oleg seven':
        print('Вхід дозволено!')
    elif x == 'Petro four':
        print('Вхід дозволено!')
    else:
        print(0/0)

except ZeroDivisionError:
    print('Упс! Помилка. Вас не знайдено у листі.')

