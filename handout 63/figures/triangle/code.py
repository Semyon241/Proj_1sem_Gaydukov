from math import sqrt

_a = 7
_b = 2
_c = 8


def triangle_perimeter(first=_a, second=_b, third=_c):
    return first + second + third


def triangle_area(first=_a, second=_b, third=_c):
    per = (first + second + third)
    return sqrt(per * (per - first) * (per - second) * (per - third))
