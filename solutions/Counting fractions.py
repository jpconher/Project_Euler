# Problem 72

import numpy as np

def sieve_of_eratosthenes(n):
    ''' get all primes <= n '''
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def prime_factors(x,list_primes):
    ''' return prime factors of x '''
    factors = []
    for a in list_primes:
        if a > x**0.5:
            break
        if x % a == 0:
            factors.append(a)
            while x % a == 0:
                x = int(x/a)
    if x > 1:
        factors.append(x)
    return factors            
        
def totient(n, prime_divisors):
    ''' calculate the totient function of the number n given its prime divisors '''
    return int(round(n*np.prod([1-1/p for p in prime_divisors]), 0))
                            
# upper limit of d
n = 10**6

# obtain primes all primes <= n/2 (better efficiency for computing prime factors)
list_primes = sieve_of_eratosthenes(int(n/2) + 1)

# solution count
red_prop_func_count = 0

for d in range(2, n + 1):
    # obtain prime_factors
    factors = prime_factors(d, list_primes)
    if factors == [d]: # prime 
        # when d is prime all n from 1 to d-1 are coprimes and, thus, part of the solution
        red_prop_func_count += d - 1
    else: # not a prime
        # only coprimes n will be part of the solution
        red_prop_func_count += totient(d, factors)
        
print("The solution is ", red_prop_func_count)