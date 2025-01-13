def double(x):
    """
    >>> m = map(double, [3, 5, 7])
    >>> next(m)
    ** 3 => 6 **
    6
    >>> next(m)
    ** 5 => 10 **
    10
    >>> next(m)
    ** 7 => 14 **
    14
    """
    print('**', x, '=>', 2 * x, '**')
    return 2 * x

