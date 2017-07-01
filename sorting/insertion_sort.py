#!/usr/bin/env python

from sys import argv

# Get user input as a command line argument
numbers = list(map(int, argv[1:]))

for i, num in enumerate(numbers[1:], 1):
    j = i - 1

    while j >= 0 and numbers[j] > num:
        numbers[j + 1], numbers[j] = numbers[j], num
        j = j - 1

# Print sorted list of numbers
print(numbers)
