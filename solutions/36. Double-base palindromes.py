# Problem 36

def base_y (x,y):
    x_base_y = ""
    for i in y[::-1]:
        if x >= i:
            x_base_y += str(1)
            x -= i
        else:
            x_base_y += str(0)
    return int(x_base_y)
    
# base 2
y = [1]
while y[-1]*2 < 1000000:
    y.append(y[-1]*2)

palindromes = []
for i in range(1,10**6):
    if i == int(str(i)[::-1]):
        if base_y(i,y) == int(str(base_y(i,y))[::-1]):
            palindromes.append(i)

    
