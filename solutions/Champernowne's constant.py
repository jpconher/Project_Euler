# Problem 40

import math

# vector containing the positions of interest
positions = [1,10,100,1000,10000,100000,1000000]

# dictionary containing position-digit
pos_dig = {}

i = 1
length_dec = 0
while length_dec <= 1000000:
    for j in str(i):
        length_dec += 1
        if length_dec in positions:
            pos_dig[length_dec] = int(j)
    i += 1
    
# return value of product
print(math.prod(pos_dig.values()))

        
    
