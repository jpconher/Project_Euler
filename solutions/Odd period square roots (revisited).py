# Problem 64

def scf(n):
    ''' Get a0, a1, a2,..., an of the simple continued fraction
    representation for a square root '''
    if n < 0:
        return "Square root does not exist"
    else:
        a = [int(n**0.5)]
        if n == a[0]**2: # perfect square
            return a
        else:
            m = a[-1]
            den = 1
            while a[-1] != 2*a[0]:
                num = n**0.5 + m
                den = (n - m**2)/den
                a.append(int(num/den))
                m = a[-1]*den - m
            return [a[0], tuple(a[1:])]
        
odd_period = sum(1 for i in range(1, 10000) if (i**0.5 % 1 != 0) and (len(scf(i)[1]) % 2 != 0))
    
print("Number of odd periods:", odd_period)
