#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Given a number n, this method calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if type(n) is not int:
        return 0
    if n <= 1:
        return 0
    ch = 1
    operations = 0
    cp = 1
    while ch < n:
        if n % ch == 0:
            cp = ch
            operations += 1
        if ch != n:
            ch = ch + cp
            operations = operations + 1
        else:
            break
    return operations
