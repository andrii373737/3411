
try:
    x = int(input('Введіть чисельник : '))
    y = int(input('Введіть знаменник : '))
    if x == 0:
        print(0/0)
    else:
        r = (y/x)
        if y == 0:
            print(0/0)
        else:
            print(y/x)

except ZeroDivisionError:
    print(' ERROR _-* We can`t calculate it with zero *-_ ERROR ')

#



