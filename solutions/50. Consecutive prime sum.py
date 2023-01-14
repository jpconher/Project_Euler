# Problem 50

def is_prime(x,primes):
    for a in primes:
        if x % a == 0:
            return False
        if a > x**0.5:
            return True

primes = [2,3]
i = 1
while sum(primes[-22:]) < 10**6: # it is known that 21 consecutive primes sum a prime < 10**3
    for j in [6*i-1,6*i+1]:
        if is_prime(j,primes):
            primes.append(j)
    i += 1

candidate = {}
for i in range(1,len(primes)):
    for j in range(0,i):
        if sum(primes[j:-(i-j)]) > 10**6:
            break
        elif is_prime(sum(primes[j:-(i-j)]),primes):
            candidate['prime'] = sum(primes[j:-(i-j)])
            candidate['length'] = len(primes[j:-(i-j)])
            break
    if len(candidate) > 0:
        break