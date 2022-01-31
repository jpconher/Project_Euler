# Problem 12

import math

def check_prime(candidate,primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

def prime_factors(number):
    factors = []
    while number % 2 == 0: #treat 2 & 3 as separate cases
        number = number/2
        factors.append(2)
    while number % 3 == 0:
        number = number/3
        factors.append(3)
    i = 1
    while number > 1:
        candidates = [6*i-1,6*i+1] #all primes > 3 can be written in that form
        for candidate in candidates:
            if check_prime(candidate, factors): 
                while number % candidate == 0:
                    number = number/candidate
                    factors.append(candidate)
        i += 1
    return factors

def number_factors(prime_fact):
    power_prime_fact = []
    for f in set(prime_fact):
        power_prime_fact.append(prime_fact.count(f)+1)
    return math.prod(power_prime_fact)
        
#the number of factors of an integer is given by \prod_{i=1}^{r}(a_{i}+1) 
#where r is the number of prime factors and a_{i} is the power of prime i. 
        
i = 2
element = 1
while True:
    if number_factors(prime_factors(element)) > 500:
        print("The first element in the sequence to have over 500 factors is", 
              element)
        break
    element += i
    i += 1
        
