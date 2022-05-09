
import unittest
from python.my_fraction import MyFraction

class TestMyFraction(unittest.TestCase):
    def test_init(self):
        # normal fraction
        frac = MyFraction(23, 29)
        self.assertEqual(frac.numerator, 23)
        self.assertEqual(frac.denominator, 29)

        # divide 0
        self.assertRaises(ValueError, MyFraction, 2, 0)
    
    def test_equal(self):
        self.assertEqual(MyFraction(1, 3), MyFraction(1, 3))
        self.assertEqual(MyFraction(-2, 5), MyFraction(2, -5))
        self.assertEqual(MyFraction(3, 5), MyFraction(27, 45))

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
        self.assertEqual(MyFraction(1, 2).divide(MyFraction(2,-2)), MyFraction(-16, 32))

    def test_reduce(self):
        self.assertEqual(MyFraction(7, 13).reduce(), MyFraction(7, 13))
        self.assertEqual(MyFraction(-10, 15).reduce(), MyFraction(-2, 3))
        self.assertEqual(MyFraction(16, 20).reduce(), MyFraction(4, 5))
# END OF TEST CLASS

if __name__ == '__main__':
    unittest.main()