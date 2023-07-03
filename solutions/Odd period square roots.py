# Problem 65

from decimal import Decimal, getcontext
getcontext().prec = 250

def scf(n):
    ''' get a0, a1, a2,..., an of the simple continued fraction
    representation for a square root '''
    if n < 0:
        return "square root does not exist"
    elif n**0.5 % 1 == 0:
        return [int(n**0.5)]
    else:
        a = [int(n**0.5)]
        reciprocal = [Decimal('1') / (Decimal(str(n))**Decimal(0.5) % Decimal('1'))] 
        while True:
            a.append(int(reciprocal[-1]))
            reciprocal.append(Decimal('1') / (reciprocal[-1] % Decimal('1')))
            if round(reciprocal[-1], 5) == round(reciprocal[0], 5):
                return [a[0], tuple(a[1:]), reciprocal] 
          
odd_period = 0
for i in range(1,10000):
    # perfect square numbers
    if i**0.5 % 1 == 0:
        continue
    elif len(scf(i)[1]) % 2 != 0:
        odd_period += 1