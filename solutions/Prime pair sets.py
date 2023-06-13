# Problem 60

def is_prime(x, primes):  
    if x < 5 and x != 2 and x != 3:
        return False
    elif x%2 == 0 or x%3 == 0:
        return False # even
    else:
        if max(primes) > x**0.5:
            for a in primes:
                if x%a == 0:
                    return False
                if a > x**0.5:
                    break
        else:
            i = 1
            while 6*i-1 <= x**0.5:
                if x%(6*i-1) == 0 or x%(6*i+1) == 0:
                    return False
                i += 1
    return True

def has_property(candidate,prime,primes):
    if candidate == 2 or candidate == 5:
        return False # 2 and 5 cannot belong to any set
    elif (is_prime(int(str(candidate)+str(prime)),primes) and 
        is_prime(int(str(prime)+str(candidate)),primes)) != True:
            return False
    return True

primes = [2,3]
candidates = []
i = 1
result = []
while not result:
    for j in [6*i-1,6*i+1]:
        if is_prime(j,primes) and not result:
            primes.append(j)
            # check pairs
            pairs_j = [k for k in primes[:-1] if has_property(k, j, primes)] 
            # check among combinations
            for candidate in candidates: 
                if all(c in pairs_j for c in candidate):
                    candidates.append(candidate+[j]) 
                    if len(candidates[-1]) == 5:
                        result = candidates[-1]
                        break
            # add pairs
            for k in pairs_j:
                candidates.append([k,j])
    i += 1