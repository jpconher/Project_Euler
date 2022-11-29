# Problem 47

import time
start_time = time.time()

def is_prime(x,list_primes):
    for a in list_primes:
        if x % a == 0:
            return False
        if a > x**0.5:
            return True
    
def prime_factors(x,list_primes):
    factors = []
    while True:
        for a in list_primes:
            while x % a == 0:
                factors.append(a)
                x = x/a
                if x == 1:
                    return factors

len_four = 0
candidate = 3
list_primes = [2]
while len_four < 4:
    if is_prime(candidate,list_primes):
        list_primes.append(candidate)
    else:
        if len(set(prime_factors(candidate,list_primes))) == 4:    
            len_four += 1
            candidate += 1
            continue
    candidate += 1
    len_four = 0
    
print(candidate-4)
    
print("--- %s seconds ---" % (time.time() - start_time))
