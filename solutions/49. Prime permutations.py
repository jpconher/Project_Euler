# Problem 49

def is_prime(x,primes):
    for a in primes:
        if x % a == 0:
            return False
        if a > x**0.5:
            return True
        
primes = [2,3]
for i in range(1,int(10001/6)):
    if is_prime(6*i-1,primes):
        primes.append(6*i-1)
    if is_prime(6*i+1,primes):
        primes.append(6*i+1)
        
prime_candidates = sorted([i for i in primes if i > 1000], reverse = True)

while len(prime_candidates) > 2:
    prime_1 = prime_candidates.pop()
    for prime_2 in [x for x in prime_candidates if set(str(x)) == set(str(prime_1))]:
        candidate = (prime_2 - prime_1) + prime_2
        if set(str(candidate)) == set(str(prime_2)) and candidate in prime_candidates:
            print(prime_1,prime_2,candidate)