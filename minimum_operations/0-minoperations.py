#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start with the smallest prime divisor

    while divisor <= math.sqrt(n):
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations    
