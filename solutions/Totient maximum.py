''' The solution can be obtained without the need of an algorithm by noticing that the
more distinct prime factors a number has, the smaller the number of relative primes it will
have. Then, the solution is just 2*3*5*7*11*13*17 '''

def get_divisors(x):
    divisors = []
    i = 2
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            divisors.append(i)
    if x > 1:
        divisors.append(x)
    return divisors	
    
# set n
n = 1000000

primes = [2,3,5,7,11,13,17]

# dictionary to store solution candidates
candidates = {}

# compute relative primes for all i <= n
for i in range(2, n + 1):
    divisors = get_divisors(i)
    if divisors == [i]: # prime number
        continue 
    if len(divisors) == len(set(divisors)) and all(x in primes for x in divisors): # distinct prime factors 
        # apply Euler's totient function to get number of relative primes
        relative_primes = i
        for p in divisors:
            relative_primes = relative_primes*(1-1/p)
    else:
        continue
    candidates[i] = i / relative_primes

print(max(candidates, key = lambda x: candidates[x]))
