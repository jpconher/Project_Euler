''' Things to consider:
- Prime numbers cannot be part of the solution (totient of n for n a prime 
  number equals n-1 which is not a permutation of n).
- 2,3,5,7 cannot be prime divisors of the solution because n/phi(n) would be
  greater than that of the candidate 87109. 
'''
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

def get_divisors(x, primes):
    ''' Get divisors of x using precomputed primes '''
    divisors = []
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            while x % p == 0:
                x //= p
            divisors.append(p)
    if x > 1:
        divisors.append(x)
    return divisors

def totient(n, prime_divisors):
    ''' calculate the totient function of the number n given its prime divisors '''
    return int(round(n*np.prod([1-1/p for p in prime_divisors]), 0))

def permutation(x, y):
    '''Check if numbers x and y are a permutation.'''
    return sorted(str(x)) == sorted(str(y))
    
# set n
n = 10000000

# get primes <= n
primes = sieve_of_eratosthenes(int(n**0.5)+1) 

# dictionary to store solution candidates
candidate = [87109, 79180, 87109/79180] # [n, phi(n), n/phi(n)]

# compute relative primes for all i <= n
for i in range(3, n, 2): # even numbers cannot be part of the solution
    if any(i % p == 0 for p in [3,5,7]): # cannot be part of the solution if divisible by (2,) 3, 5, or 7
        continue
    else:
        divisors = get_divisors(i, primes)
        if divisors != [i]: # not a prime number
            tot = totient(i, divisors)
            # check if n/phi(n) is smaller than current candidate and totient is a permutation
            if i/tot < candidate[2] and permutation(i, tot):
                    candidate = [i, tot, i/tot]

print("Solution:", candidate[0])