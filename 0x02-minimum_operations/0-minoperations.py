#!/usr/bin/python3
"""
Module for calculating minimum operations.
"""

def minOperations(n):
    """
    Returns the minimum number of operations needed to reach n 'H' characters
    :param n: integer, the target number of characters
    :return: integer, minimum number of operations
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor  # Add the divisor to operations
            n //= divisor  # Divide n by the divisor
        divisor += 1

    return operations