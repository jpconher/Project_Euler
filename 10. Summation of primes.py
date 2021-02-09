# Problem 10

import math

def check_prime(candidate,primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
        if math.sqrt(candidate) < prime: #a composite number always have a prime factor smaller than its sqrt
            return True
    return True

#palindromes = list((x for x in candidates if palindrome(x)))

def generate_primes(n):
  if n == 1:
    return 2
  elif n == 2:
    return [2,3]
  else:
    primes = [2,3]
    i = 1
    while primes[-1] < n:
        for candidate in [6*i-1,6*i+1]: #all primes greater than 3 can be written in that form
            if check_prime(candidate, primes):
                primes.append(candidate)
        i += 1
    return primes[:-1]

sum_primes = sum(generate_primes(2000000))