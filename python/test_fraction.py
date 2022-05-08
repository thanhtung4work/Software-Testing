import unittest


import unittest
import my_fraction

class TestMyFraction(unittest.TestCase):
    def test_add(self):
        frac1 = my_fraction.MyFraction(2, 2)
        frac2 = my_fraction.MyFraction(4, 2)
        result = frac1.add( frac2 ).normalize()
        self.assertEqual(result, my_fraction.MyFraction(3, 1))
    
    def test_substract(self):
        frac1 = my_fraction.MyFraction(3, 2)
        frac2 = my_fraction.MyFraction(1, 2)
        result = frac1.substract( frac2 ).normalize()
        self.assertEqual(result, my_fraction.MyFraction(1, 1))

    def test_multiply(self):
        frac1 = my_fraction.MyFraction(3, 2)
        frac2 = my_fraction.MyFraction(1, 2)
        result = frac1.substract( frac2 ).normalize()
        self.assertEqual(result, my_fraction.MyFraction(3, 4))

    def test_divide(self):
        frac1 = my_fraction.MyFraction(3, 2)
        frac2 = my_fraction.MyFraction(1, 2)
        result = frac1.substract( frac2 ).normalize()
        self.assertEqual(result, my_fraction.MyFraction(3, 1))

if __name__ == '__main__':
    unittest.main()