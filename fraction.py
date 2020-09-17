from math import gcd

class Fraction:
    def __init__(self,n = 1,d = 1): #We use n for numerator and d for denominator
        if d == 0 :
            raise ValueError("Division by 0 !")
        else :
                temp = gcd(n,d)
                if n > 0 and d > 0 or n < 0 and d < 0 :
                    a = int(n/temp)
                    b = int(d/temp)
                elif n < 0 :
                    a = int(n/temp)
                    b = int(d/temp)
                else :
                    a = -int(n/temp)
                    b = -int(d/temp)
                self.n = a
                self.d = b

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d
    
    def __lt__(self,other):
        d1 = self.n * other.d
        d2 = other.n * self.d
        return d1 < d2
    
    def __gt__(self,other):
        return not (self < other)

    def __mul__(self,other):
        return Fraction(self.n*other.n,self.d*other.d)
    
    def __add__(self,other):
        a = self.n*other.d + other.n*self.d
        b = self.d * other.d
        return Fraction(a,b)
    
    def __str__(self):
        return str(self.n)+"/"+str(self.d)

    def add(self,other):
        return self + other
    
    def multiply(self,other):
        return self * other

f1 = Fraction(1,-3)
f2 = Fraction(1,3)

print(f1<f2)