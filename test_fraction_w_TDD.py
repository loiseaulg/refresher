
from math import gcd
import pytest

class Fraction():
    def __init__(self, n = 1, d = 1):
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
                    a = - int(n/temp)
                    b = - int(d/temp)
                self.n = a
                self.d = b
    
    def __eq__(self,o):
        return self.n == o.n and self.d == o.d
    
    def __gt__(self,o):
        n1 = self.n * o.d
        n2 = o.n * self.d
        return n1 > n2
    
    def __add__(self,o):
        a = self.n*o.d + o.n*self.d
        b = self.d * o.d 
        return Fraction(a,b)
    
    def __mul__(self,o):
        return Fraction(self.n * o.n, self.d * self.d)
    
    def __str__(self):
        return str(self.n)+"/"+str(self.d)
        
#=======================================================================
def test_faction_init():
    f1 = Fraction()
    f2 = Fraction()
    assert f1 == f2

def test_faction_simplification():
    f1 = Fraction(22,11)
    assert f1.n == 2 and f1.d == 1

def test_division_by_zero():
    with pytest.raises(ValueError) as e :
        f = Fraction(1,0) 
    assert e

def test_negative_deno():
    f1 = Fraction(1,-2)
    assert f1.n < 0

def test_greater_than():
    f1 = Fraction(1,2)
    f2 = Fraction(1,4)
    assert f1 > f2

#def test_add():
#    f1 = Fraction(21,22)
#    f2 = Fraction(33,17)
#    assert f1 + f2 == Fraction(335,374)

def test_ui():
    assert Fraction(3,4) + Fraction(1,2) == Fraction(5,4)

def test_string():
    assert str(Fraction(3,4)) == "3/4"

def test_multiply():
    assert Fraction(1,2)*Fraction(1,2) == Fraction(1,4)






#=======================================================================
