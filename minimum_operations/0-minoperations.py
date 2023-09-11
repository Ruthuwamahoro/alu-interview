#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    if n <= 1:
        return 0

    # Create a list to store the minimum operations needed for each number from 0 to n
    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')  # Initialize with positive infinity
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)
    
    return operations[n] if operations[n] != float('inf') else 0
