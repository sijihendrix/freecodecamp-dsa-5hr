import random
import sys

from load import load_numbers 

numbers = load_numbers(sys.argv[1])

# print(numbers)

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True


def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values

print(bogo_sort(numbers))