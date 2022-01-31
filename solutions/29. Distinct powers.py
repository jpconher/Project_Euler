# Problem 29

import math

# compute repeated terms between numbers a and a^b
def repeated(b): 
    return(len(range(b*2,math.floor(100/b)*b+1,b)))
    
# create vector to store result
repeated_terms = 0

for a in range(2,100+1):
    if a**2 > 100:
        break
    for b in range(2,100+1):
        if a**b <= 100:
            repeated_terms += repeated(b)  
        else:
            break
        
# print number of distinct terms
print(99*99-(repeated_terms))
    
    