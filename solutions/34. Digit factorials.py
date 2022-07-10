# Problem 34

# store factorials in dict
fact = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

# solution
sol = []

# candidate
for i in range(3,10**6):
    if i == sum([fact[int(x)] for x in list(str(i))]):
        sol.append(i)


    
    
    
        
