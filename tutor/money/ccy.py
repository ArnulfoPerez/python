"""
The class "Ccy" can be used to define money values in various currencies.
A Ccy instance has the string attributes 'unit'
(e.g. 'CHF', 'CAD' od 'EUR' and the 'value' as a float.
A currency object consists of a value and the corresponding unit.
"""


class Ccy:
    currencies = {
        'CHF': 1.0821202355817312,
        'CAD': 1.488609845538393,
        'GBP': 0.8916546282920325,
        'JPY': 114.38826536281809,
        'EUR': 1.0,
        'USD': 1.11123458162018
    }

    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def changeTo(self, new_unit):
        """
        An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (
            self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
        Defines the '+' operator.
        If other is a CCy object the currency values 
        are added and the result will be the unit of 
        self. If other is an int or a float, other will
        be treated as a Euro value. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] *
                 Ccy.currencies[self.unit])
        return Ccy(x + self.value, self.unit)

    def __iadd__(self, other):
        """
        Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] *
                 Ccy.currencies[self.unit])
        self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res

    # __sub__, __isub__ and __rsub__ can be defined analogue


x = Ccy(10, "USD")
y = Ccy(11)
z = Ccy(12.34, "JPY")
z = 7.8 + x + y + 255 + z
print(z)

lst = [Ccy(10, "USD"), Ccy(11), Ccy(12.34, "JPY"), Ccy(12.34, "CAD")]

z = sum(lst)

print(z)
