
import unittest
import my_fraction

class TestMyFraction(unittest.TestCase):
    def test_add(self):
        frac1 = my_fraction.MyFraction(2, 2)
        frac2 = my_fraction.MyFraction(4, 2)
        result = frac1.add( frac2 ).reduce()
        self.assertEqual(result, my_fraction.MyFraction(3, 1))
    
    def test_substract(self):
        frac1 = my_fraction.MyFraction(212, 2)
        frac2 = my_fraction.MyFraction(111, 2)
        result = frac1.substract( frac2 ).reduce()
        self.assertEqual(result, my_fraction.MyFraction(101, 2))

    def test_multiply(self):
        frac1 = my_fraction.MyFraction(3, 2)
        frac2 = my_fraction.MyFraction(1, 2)
        result = frac1.multiply(frac2).reduce()
        self.assertEqual(result, my_fraction.MyFraction(3, 4))

    def test_divide(self):
        frac1 = my_fraction.MyFraction(3, 2)
        frac2 = my_fraction.MyFraction(2, 2)
        result = frac1.divide( frac2 ).reduce()
        self.assertEqual(result, my_fraction.MyFraction(6, 4))

if __name__ == '__main__':
    unittest.main()