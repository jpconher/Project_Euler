# Problem 46

def is_prime(x,list_primes):
    for a in list_primes:
        if x % a == 0:
            return False
        if a > x**0.5:
            return True
        
def is_goldbach(x,list_primes):
    for a in list_primes:
        if (((x-a)/2)**0.5).is_integer():
            return True
    return False

candidate = 3
list_primes = [2]
while True:
    if is_prime(candidate,list_primes):
        list_primes.append(candidate)
    elif 1 - is_goldbach(candidate,list_primes):
        print(candidate)
        break
    candidate += 2
    
