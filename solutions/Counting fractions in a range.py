# Problem 73

import math

def gcd_euclid(n:int, d:int) -> int:
    '''Computes the greates common divisor using the Euclid algorithm '''
    if (n == 0) & (d != 0):
        return d
    elif (n != 0) & (d == 0):
        return n
    elif n == d:
        if n == 0:
            raise Exception("Undetermined GCD (any number is a divisor)")
        else:
            return n
    elif n < d:
        while True:
            remainder = d % n
            if remainder == 0:
                return n
            else:
                d = n
                n = remainder
    elif n > d:
        while True:
            remainder = n % d
            if remainder == 0:
                return d
            else:
                n = d
                d = remainder    

# upper limit of d
n = 12000

# number of fractions part of the solution
solution = 0

for den in range(2, n+1):
    if den % 3 == 0:
        lower_bound = int(den/3) + 1
    else:
        lower_bound = math.ceil(den/3)
    upper_bound = math.ceil(den/2)
    for num in range(lower_bound, upper_bound):
        if gcd_euclid(num,den) == 1:
            solution += 1
