# Problem 71

def gcd_euclid(n:int, d:int) -> int:
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
    
d = 10**6
candidate = [0, 1] # initialise

for den in range(2, d+1):
    if den == 7:
        continue
    else:
        num = den*3//7 # closest num/den fixing den
        if num/den > candidate[0]/candidate[1]: # greater than previous candidate
            if gcd_euclid(num, den) == 1:
                    candidate = [num, den]