#!/usr/bin/python3
"""
Main file for testing the minOperations function
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))