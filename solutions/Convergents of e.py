# Problem 65

from mpmath import mp
mp.dps = 200  # 100 decimal places of precision

def scf(n, k):
    ''' Get first k components of the simple continued fraction 
    a0, a1, a2,..., ak-1 representation of positive real number n '''
    if n <= 0:
        return "Only positive real numbers"
    else:
        a = [int(n)]
        if n == a[0]: # positive integer
            return a
        else:
            m = a[-1]
            den = 1
            while len(a) < k:
                num = n + m
                den = (n**2 - m**2)/den
                a.append(int(num/den))
                m = a[-1]*den - m
            return [a[0], tuple(a[1:])]

def continued_fraction(a, k):
    ''' Calculates the numerator and denominator of the simple continued
    fraction (scf) using as input a vector of the components of the scf
    a = [a0, (a1, a2, a3,...ak)] using the first k terms where k <= k+1 '''
    if len(a[1]) + 1 < k:
        return "Not enough components in vector a"
    else:
        if len(a) == 1:
            return [a[0], 1]
        elif len(a[1]) == 1:
            return [a[1][0]*a[0] + 1, a[1][0]]
        i = 3
        num = [a[0], a[1][0]*a[0] + 1]
        den = [1, a[1][0]]
        while i <= k:
            num.append(a[1][i-2]*num[-1] + num[-2])
            den.append(a[1][i-2]*den[-1] + den[-2])
            i += 1
        return(num[-1], den[-1])
    
n = mp.e
num, den = continued_fraction(scf(n, 100), 100)
print("the sum of the digits in the numerator is", 
      sum([int(i) for i in list(str(num))]))      