# Problem 37

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
trun_primes = [a for a in primes if len(str(a)) > 1 and len([b for b in list(str(a))[1:] if int(b) in [0,2,4,6,8]]) == 0 \
              and len([b for b in list(str(a))[0] if int(b) in [1,4,6,8,9]]) == 0]
for i in trun_primes.copy():
    for j in range(1,len(str(i))):
        if int(str(i)[j:]) in primes and int(str(i)[:j]) in primes:
            continue
        else:
            trun_primes.pop(trun_primes.index(i))
            break
