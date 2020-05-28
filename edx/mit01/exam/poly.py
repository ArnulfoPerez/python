def general_poly(poly):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    degree = len(poly) - 1
    return lambda x: sum((x**n)*poly[degree - n] for n in range(degree + 1))

assert general_poly([1, 2, 3, 4])(10) == 1234
                   