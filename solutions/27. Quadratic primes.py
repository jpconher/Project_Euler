# Problem 27

import math

def check_prime(candidate,primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
        if math.sqrt(candidate) < prime: # a composite number always have a prime factor smaller than its sqrt
            return True
    return True

def generate_primes(n):
    if n < 2:
        return "No prime number smaller than 2"
    elif n == 2:
        return 2
    elif n == 3:
        return [2,3]
    else:
        primes = [2,3]
        i = 1
        while primes[-1] < n:
            for candidate in [6*i-1,6*i+1]: # all primes greater than 3 can be written in that form
                if check_prime(candidate, primes):
                    primes.append(candidate)
            i += 1
    return([prime for prime in primes if prime < n])

# generate all primes smaller than 999^2 + 999*999 + 999 
primes = generate_primes(999^2+999*999+1000)

# b has to be prime itself
b_candidates = [prime for prime in primes if abs(prime) < 1001]

results = {}

for b in b_candidates:
    for a in range(-b,1000,2):    # if a even at most prime for n = 0
        n = 1    
        while True:
            if n**2+a*n+b in primes:
                n += 1
            else:
                results[a,b] = n-1
                break
                    
print(max(results, key=results.get))                 

