# Problem 45

def triangle(n):
    return int(n*(n+1)/2)

def check_pentagonal(n):
    return ((1+(1+24*n)**0.5)/6).is_integer()

def check_hexagonal(n):
    return ((1+(1+8*n)**0.5)/4).is_integer()

n = 286
while True:
    if (check_pentagonal(triangle(n)) and check_hexagonal(triangle(n))):
        break
    else:
        n += 1
        
print(triangle(n))

