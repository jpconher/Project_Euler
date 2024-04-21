''' The solution can be obtained without the need of an algorithm by noticing that the
more distinct prime factors a number has, the smaller the number of relative primes it will
have. Then, the solution is just 2*3*5*7*11*13*17 '''

import time
start_time = time.time()

def get_divisors(x, primes):
    divisors = []
    for i in primes:
        if x % i == 0:
            while x % i == 0:
                x //= i
            divisors.append(i)
        elif i**2 > x:
            break
    if x > 1:
        divisors.append(x)
        if x > primes[-1]:
            primes.append(x)
    return divisors, primes
    
# set n
n = 1000000

primes = [2]

primes_solution = [2,3,5,7,11,13,17]

# dictionary to store solution candidates
candidates = {}

# compute relative primes for all i <= n
for i in range(2, n + 1):
    divisors, primes = get_divisors(i, primes)
    if divisors == [i]: # prime number
        continue 
    if all(x in primes_solution for x in divisors): # distinct prime factors 
        # apply Euler's totient function to get number of relative primes
        relative_primes = i
        for p in divisors:
            relative_primes = relative_primes*(1-1/p)
    else:
        continue
    candidates[i] = i / relative_primes

print(max(candidates, key = lambda x: candidates[x]))

print("--- %s seconds ---" % (time.time() - start_time))
