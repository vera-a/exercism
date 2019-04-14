from __future__ import division

from fractions import Fraction


class Rational:

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self = Fraction.from_float(self)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return ((self.numer * other.denom) + (self.denom * other.numer)) / (other.numer * other.denom) 

    def __sub__(self, other):
        return ((self.numer * other.denom) - (self.denom * other.numer)) / (other.numer * other.denom)

    def __mul__(self, other):
        return (self.numer * self.denom) / (other.numer * other.denom)

    def __truediv__(self, other):
        return (self.numer * other.denom ) / (self.denom * other.numer) 

    def __abs__(self):
        return abs(self)

    def __pow__(self, power):
        if power > 0:
            return (self.numer * power) / (self.denom * power) 
        elif power == 0:
            return 1
        else:
            return (self.denom * power) / (self.numer * power)

    def __rpow__(self, base):
        pass
        
