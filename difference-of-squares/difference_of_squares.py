import math
from functools import reduce

def square_of_sum(count):
    numbers = [number for number in range(1, count + 1)]
    sum = reduce(lambda x, y: x+y, numbers)
    return sum ** 2

    
def sum_of_squares(count):
    squared = [number ** 2 for number in range(1, count + 1)]
    return reduce(lambda x, y: x+y, squared)
    

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
