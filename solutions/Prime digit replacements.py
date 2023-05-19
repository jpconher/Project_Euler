# Problem 51

from itertools import combinations

def is_prime(x,primes):
    for a in primes:
        if x % a == 0:
            return False
        if a > x**0.5:
            return True

def assign_to_family(family,prime_families,prime):
    if family in prime_families:
        prime_families[family].append(prime)
    else:
        prime_families[family] = [prime]
    if len(prime_families[family]) == 8:
        global smallest_prime
        smallest_prime = min(prime_families[family])

def family_combinations(family,prime_families,j):
    indices = [pos for pos, char in enumerate(family) if char == "X"]
    for i in range(1,len(indices)+1):
        for k in combinations(indices,i):
            prime_list = list(str(j))
            for index in list(k):
                prime_list[index] = "X"
            assign_to_family(''.join(prime_list),prime_families,j)

primes = [2,3]
prime_families = {}

i = 1
smallest_prime = 0
while smallest_prime == 0: 
    for j in [6*i-1,6*i+1]:
        if is_prime(j,primes):
            primes.append(j)
            for x in set(str(j)):
                family = str(j).replace(x,"X")
                if family.count("X") > 1:
                    family_combinations(family,prime_families,j)
                else:
                    assign_to_family(family,prime_families,j)                           
    i += 1
