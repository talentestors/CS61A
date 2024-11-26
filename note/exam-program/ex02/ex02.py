def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """Return the real part of the square root of x."""
    return if_(x >= 0, sqrt(x), 0)
#    if x >= 0:
#        return sqrt(x)
#    else:
#        return 0

