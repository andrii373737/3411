import unittest
from lesson8 import sum

class MT(unittest.TestCase):
    def test_args(self):
        self.assertEqual(sum(2, 1000), 1002)

if __name__ == '__main__':
    unittest.main()