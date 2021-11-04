from fractions import Fraction


def string_to_float(string):
    return float(sum(Fraction(s) for s in string.split()))
