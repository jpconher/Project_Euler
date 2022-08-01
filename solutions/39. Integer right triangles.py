# Problem 39

import math 

# store solutions
solutions = {}

for a in range(1,500):
    for b in range (a,500):
        if a + b + math.sqrt(a**2+b**2) > 1000:
            break
        else:
            if int(math.sqrt(a**2+b**2)) == math.sqrt(a**2+b**2):
                if int(a+b+math.sqrt(a**2+b**2)) in solutions.keys():
                    solutions[int(a+b+math.sqrt(a**2+b**2))] += [[a,b,int(math.sqrt(a**2+b**2))]]
                else:
                    solutions[int(a+b+math.sqrt(a**2+b**2))] = [[a,b,int(math.sqrt(a**2+b**2))]]

# return perimeter with largest number of solutions
res = {k: v for k, v in solutions.items() if len(v) == max(map(len, solutions.values()))}


                
