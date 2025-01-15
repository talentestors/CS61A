def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

