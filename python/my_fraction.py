
from math import gcd

class MyFraction:
    numerator = 1
    denominator = 1
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if(denominator < 0 ):
            self.denominator = denominator * -1
            self.numerator *= -1
        elif(denominator == 0):
            raise Exception("Denominator cannot be zero")
        else:
            self.denominator = denominator

    def add(self, frac):
        result = MyFraction(1, 1)
        if(self.denominator == frac.denominator):
            result.numerator = self.numerator + frac.numerator
            result.denominator = self.denominator
        else:
            result.numerator = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
            result.denominator = self.denominator * frac.denominator
        return result
    
    def substract(self, frac):
        frac = MyFraction(frac.numerator * -1, frac.denominator)
        return self.add(frac)

    def multiply(self, frac):
        result = MyFraction(1, 1)
        result.numerator = self.numerator * frac.numerator
        result.denominator = self.denominator * frac.denominator
        return result

    def divide(self, frac):
        frac = MyFraction(frac.denominator, frac.numerator)
        return self.multiply(frac)

    def reduce(self):
        divider = gcd(self.numerator, self.denominator)
        reduced = MyFraction(self.numerator // divider, self.denominator // divider)
        return reduced

    def __eq__(self, __o: object) -> bool:
        y = self.numerator * __o.denominator - self.denominator * __o.numerator
        if y == 0:
            return True
        return False
    
    def __str__(self) -> str:
        return "{0}/{1}".format(self.numerator, self.denominator)
