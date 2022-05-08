class MyFraction:
    numerator = 1
    denominator = 1
    def __init__(self, numerator, denominator):
        self.numerator = numerator
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

    def normalize(self):
        if(self.numerator % self.denominator == 0):
            return MyFraction( int(self.numerator / self.denominator), 1 )
        else:
            return self

    def __eq__(self, __o: object) -> bool:
        if(self.numerator % __o.numerator == 0):
            if(self.denominator % __o.denominator == 0):
                return True
        if(__o.numerator % self.numerator == 0):
            if(__o.denominator % self.denominator == 0):
                return True
        return False
    
    def __str__(self) -> str:
        return "{0}/{1}".format(self.numerator, self.denominator)
