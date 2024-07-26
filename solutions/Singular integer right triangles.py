# Problem 75

def euclid_formula(m:int, n:int) -> int:
    ''' given integers m,n with m>n>0 returns the perimeter
    of the corresponding Pythegorean triple '''
    # check if m and n are integers
    if type(m) != int or type(n) != int:
        raise Exception("At least one of the inputs is not integer type.")
    # check if m>n>0
    elif (n >= m) or (n <= 0 or m <= 0):
        raise Exception("Please, make sure m > n > 0.")
    else:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        return a+b+c
    
def euclid_gcd(a:int, b:int) -> int:
    ''' given integers a, b with a>=b (positive integers) returns the greatest 
    common divisor using the euclid's algorithm '''
    # check if m and n are integers
    if type(a) != int or type(b) != int:
        raise Exception("At least one of the inputs is not integer type.")
    # check if a>b
    elif (b > a):
        raise Exception("Please, make sure a >= b.")
    else:
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a
            
# maximum length 
l = 1500000

# pythagorean triples
pyt_trip = {}

# compute pythagorean triples
for m in range(2, l):
    for n in range(1, m):
        # coprimes + exactly one is even guarantees primitive triples   
        if (euclid_gcd(m, n) == 1) and (sum([m % 2 == 0, n % 2 == 0]) == 1):
            triple_length = euclid_formula(m, n)
            if triple_length > l:
                break
            else:
                pyt_trip[triple_length] = pyt_trip.get(triple_length, 0) + 1
                # include all triples that derived from the primitive triple
                n = 2
                while n*triple_length <= l:
                    pyt_trip[n*triple_length] = pyt_trip.get(n*triple_length, 0) + 1
                    n += 1
                    
print("Solution:", sum([1 if x == 1 else 0 for x in pyt_trip.values()]))