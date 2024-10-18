#!/usr/bin/python3
"""
Module that calculates the minimum number of
operations needed to get exactly n H characters.
"""

def minOperations(n):
    """
    Returns the minimum number of operations required to 
    get n 'H' characters in the file.
    
    :param n: integer, the target number of 'H' characters
    :return: integer, the minimum number of operations, or 0 if n is 
    less than 2
    """
    if n < 2:
        return 0
    
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operation count
            n //= divisor  # Reduce n by dividing by the divisor
        divisor += 1
    
    return operations
