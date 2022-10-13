# Problem 43

from itertools import permutations

def check_property(digits,divisors):
    if digits[-1] % 2 == 0: 
        return False # the last property requires odd last digit
    for i in range(1,len(digits)-2):
        if int(''.join(map(str,digits[i:i+3]))) % divisors[i-1] != 0:   
            return False
    return True          
        
digits = [9,8,7,6,5,4,3,2,1,0]
divisors = [2,3,5,7,11,13,17]

# get all 0-9 pandigitals
candidates = list(permutations(digits))

has_property = []
for i in candidates:
    if check_property(i,divisors):
        has_property.append(int(''.join(map(str,i))))

print(sum(has_property))