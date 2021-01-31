# Problem 3

number = 600851475143

def check_prime(candidate,primes):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

def prime_factors(number):
    factors = []
    while number % 2 == 0: #treat 2 & 3 as separate cases
        number = number/2
        factors.append(2)
    while number % 3 == 0:
        number = number/3
        factors.append(3)
    i = 1
    while number > 1:
        candidates = [6*i-1,6*i+1] #all primes > 3 can be written in that form
        for candidate in candidates:
            if check_prime(candidate, factors): 
                while number % candidate == 0:
                    number = number/candidate
                    factors.append(candidate)
        i += 1
    return factors
        
prime_fact = prime_factors(number)
