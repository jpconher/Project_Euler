# Problem 64

from decimal import Decimal, getcontext
getcontext().prec = 250

def scf(n):
    ''' Get a0, a1, a2,..., an of the simple continued fraction
    representation for a square root '''
    if n < 0:
        return "Square root does not exist"
    elif n**0.5 % 1 == 0:
        return [int(n**0.5)]
    else:
        a = [int(n**0.5)]
        reciprocal = [Decimal('1') / (Decimal(n).sqrt() % Decimal('1'))]
        while True:
            a.append(int(reciprocal[-1]))
            reciprocal.append(Decimal('1') / (reciprocal[-1] % Decimal('1')))
            if round(reciprocal[-1], 5) == round(reciprocal[0], 5):
                return [a[0], tuple(a[1:]), reciprocal] 

def count_odd_periods(limit):
    odd_period = 0
    for i in range(1, limit+1):
        # Perfect square numbers
        if i**0.5 % 1 == 0:
            continue
        elif len(scf(i)[1]) % 2 != 0:
            odd_period += 1
    return odd_period

odd_period_count = count_odd_periods(10000)
print("Number of odd periods:", odd_period_count)
