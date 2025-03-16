def double(x):
    if isinstance(x, str):
        raise TypeError('double takes only number')
    return 2 * x

def invert(x):
    result = 1 / x
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)
    
