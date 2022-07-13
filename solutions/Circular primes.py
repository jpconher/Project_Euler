# Problem 35

import math

def is_prime(x,primes):
    for a in primes:
        if x % a == 0:
            return primes
        if a > math.sqrt(x):
            return primes.append(x)

# vector containing prime numbers
primes = [2,3]

i = 1
while 6*i-1 < 10**6:
    for j in [6*i-1,6*i+1]:
        is_prime(j,primes)
    i += 1

# candidates
circular_primes = [a for a in primes if len(str(a)) == 1 or len([b for b in list(str(a)) if int(b) in [0,2,4,6,8]]) == 0]
for i in circular_primes.copy(): 
    for j in range(len(str(i))-1):
        if int(str(i)[j+1:] + str(i)[:j+1]) not in circular_primes:
            circular_primes.pop(circular_primes.index(i))
            break
