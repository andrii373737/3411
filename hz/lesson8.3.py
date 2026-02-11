import unittest

def sum(a, b):
    return a + b

def test_sum():
    assert sum(9, 1) == 10

test_sum()
