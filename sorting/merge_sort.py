#!/usr/bin/env python

from sys import argv

# Get user input as a command line argument
numbers = list(map(int, argv[1:]))

# Merge two arrays
def merge(a, b):
    i, j = 0, 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1
    
    result = result + a[i:]
    result = result + b[j:]

    return result

# Sort the given array
def sort(array):
    mid = int(len(array) / 2)
    left, right = [], []

    if len(array) < 2:
        return array
        
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)
 
# Output sorted result
print(sort(numbers))
