def stepen_dva(number, max_degree):
    degree = 0
    number = 2
    for num in range(max_degree):
        yield number ** degree
        degree += 1


two_in_degree = stepen_dva(2,20)

for el in two_in_degree:
    print(el)


