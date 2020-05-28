# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:00:44 2017

@author: Arnulfo
"""

from forex_python.converter import CurrencyRates, CurrencyCodes

class Ccy:
    '''
    Currency converter class
    uses forex_python module
    '''

    rates = CurrencyRates()
    codes = CurrencyCodes()

    def get_other_value(self, other):
        '''
        helper function for magic add
        '''
        if isinstance(other, int) or isinstance(other, float):
            return Ccy.rates.convert(self.base, self.unit, other)
        else:
            return Ccy.rates.convert(other.unit, self.unit, other.value)

    def __init__(self, value, unit="EUR", base='EUR'):
        self.value = value
        self.unit = unit
        self.base = base

    def __str__(self):
        return "{0:}{1:5.2f}".format(
            Ccy.codes.get_symbol(self.unit), self.value) \
            + ' ' + self.unit

    def __repr__(self):
        return 'Ccy(' + str(self.value) + ', "' + self.unit + '")'

    def change_currency(self, new_unit):
        """
        An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = Ccy.rates.convert(self.unit, new_unit, self.value)
        self.unit = new_unit

    def __add__(self, other):
        """
        Defines the '+' operator.
        If other is a CCy object the currency values
        are added and the result will be the unit of
        self. If other is an int or a float, other will
        be treated as a Euro value.
        """
        return Ccy(self.get_other_value(other) + self.value, self.unit)

    def __iadd__(self, other):
        """
        Similar to __add__
        """
        self.value += self.get_other_value(other)
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != self.base:
            res.change_currency(self.base)
        return res
    # __sub__, __isub__ and __rsub__ can be defined analogue

    def __mul__(self, other):
        """
        Multiplication is only defined as a scalar multiplication,
        i.e. a money value can be multiplied by an int or a float.
        It is not possible to multiply to money values
        """
        if isinstance(other, int) or isinstance(other, float):
            return Ccy(self.value * other, self.unit)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " +
                            type(other).__name__)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.value *= other
            return self
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " +
                            type(other).__name__)

if __name__ == "__main__":
    print(Ccy(1000, "JPY") + 4.11 * Ccy(10, "CHF") + Ccy(15, "CAD"))
    