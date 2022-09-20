# Problem 41

import math

def is_prime(x,primes):
    for a in primes:
        if x % a == 0:
            return False
        if a > math.sqrt(x):
            return True
        
def next_pandigital(x):
    x_list = list(str(x))
    if len(x_list) == len(set(x_list)) & len(x_list) > 1: 
        while True:
            for i in range(2,len(x_list)+1):
                for j in x_list[-i+1::]:
                    if int(x_list[-i]) > int(j) & int(j) == max([int(a) for a in x_list[-i+1::] if int(a) < int(x_list[-i])]):
                        x_list[x_list.index(j)], x_list[-i] = x_list[-i], j
                        x_list[-i+1::] = sorted(x_list[-i+1::],reverse = True)
                        return int("".join(x_list))
            del x_list[x_list.index(max(x_list))]
            x_list = x_list[::-1]
    else:
        return "Introduce a valid pandigital number"
        
# vector containing prime numbers
primes = [2,3]

i = 1
while 6*i-1 < math.sqrt(987654321): # get primes smaller than sqrt of largest 9-digit pandigital 
    for j in [6*i-1,6*i+1]:
        if is_prime(j,primes):
            primes.append(j)
    i += 1

candidate_pandigital = 987654321
while True:
    if candidate_pandigital % 2 == 0:
        candidate_pandigital = next_pandigital(candidate_pandigital)
    elif is_prime(candidate_pandigital,primes):
        print(candidate_pandigital)
        break
    else:
        candidate_pandigital = next_pandigital(candidate_pandigital)
        
    



