# Problem 20

import math

def sum_digits(number):
    sum = 0
    for i in range(0,len(str(number))):
        sum += int(str(number)[i])
    return sum

sum = sum_digits(math.factorial(100))
    

