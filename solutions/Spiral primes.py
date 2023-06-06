# Problem 58

def is_prime(x):  
    if x < 5:
        return True if x == 2 or x == 3 else False
    elif x % 2 == 0 or x % 3 == 0:
        return False # even
    else:
        i = 1
        while 6*i-1 <= x**0.5:
            if x % (6*i-1) == 0 or x % (6*i+1) == 0:
                return False
            i += 1
        return True
    
n_primes = 0
side_length = 3 # start from square side 3
largest_last = 1 # largest number previous square 
while True:
    for corner in range(1,5):
        if is_prime(largest_last + (side_length - 1)*corner):
            n_primes += 1
    n_diagonals = 2*side_length - 1
    if n_primes/n_diagonals < 0.1:
        break
    else:
        largest_last +=  (side_length - 1)*4
        side_length += 2
    
    
    
            
        