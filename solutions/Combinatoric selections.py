# Problem 53

# if binomial_coeff(n,r*) > 10**6, then binomial_coeff(n,r) > 10**6 for n-r > r* 

from math import factorial

def binomial_coeff(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

count = 0
n = 1
while n < 101:
    if factorial(n) < 10**6: 
        n += 1
    else:
        i = 1
        while i < n:
            if binomial_coeff(n,i) > 10**6:
                count += n - 2*i + 1 
                break
            else:
                i += 1
    n += 1
    