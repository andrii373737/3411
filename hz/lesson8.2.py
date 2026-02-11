import doctest

def mul(a, b):
    '''
    >>> mul(1, 5)
    5
    >>> mul(5, 5)
    twenty five
    '''
    return a*b



if __name__ == '__main__':
    print('Testing . . .')
    doctest.testmod()