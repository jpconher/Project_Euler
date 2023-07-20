# Problem 66

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
        
def continued_fraction(a):
    ''' Calculates the numerator and denominator of the simple continued
    fraction (scf) using as input a vector of the components of the scf
    a = [a0, (a1, a2, a3,...ak)] '''
    if len(a) == 1:
        return [a[0], 1]
    elif len(a[1]) == 1:
        return [a[1][0]*a[0] + 1, a[1][0]]
    else:
        num = [a[0], a[1][0]*a[0] + 1]
        den = [1, a[1][0]]
        for i in range(3, len(a[1]) + 1):
            num.append(a[1][i-2]*num[-1] + num[-2])
            den.append(a[1][i-2]*den[-1] + den[-2])
        return(num[-1], den[-1])

largest_x = {'x': 0, 'D': 0}
for D in range(2, 1001):
    if (D**0.5).is_integer() == True:
        continue # if D perfect square there is no solution (assumption)
    else:
        scf_elements = scf(D)
        if len(scf_elements[1]) % 2 != 0: # if len(elements) odd, duplicate (see proof)
            scf_elements[1] = 2*scf_elements[1]
        x = continued_fraction(scf_elements)[0] # get numerator (x)
        if largest_x['x'] < x:
            largest_x['x'] = x
            largest_x['D'] = D  