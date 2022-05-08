
import unittest
import my_fraction
from python.my_fraction import MyFraction

class TestMyFraction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MyFraction(1, 3).add(MyFraction(3, 5)), MyFraction(14, 15))
        self.assertEqual(MyFraction(5, 9).add(MyFraction(11, 13)), MyFraction(164, 117))
    
    def test_substract(self):
        self.assertEqual(MyFraction(11, 13).substract(MyFraction(13, 17)), MyFraction(18, 221))
        self.assertEqual(MyFraction(7, 27).substract(MyFraction(2, 5)), MyFraction(19, -135))

    def test_multiply(self):
        self.assertEqual(MyFraction(6, 9).multiply(MyFraction(11, 13)), MyFraction(66, 117))

    def test_divide(self):
        self.assertEqual(MyFraction(7, 13).divide(MyFraction(2,23)), MyFraction(161, 26))

if __name__ == '__main__':
    unittest.main()