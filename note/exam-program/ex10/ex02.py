def palindrome(s):
    """Return whethyer s is the same backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    # return list(s) == list(reversed(s))
    return all([a == b for a, b in zip(s, reversed(s))])

