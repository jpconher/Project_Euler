# Problem 38

# store pandigitals
pandigital = []

for i in range(1,9999):
    k = int(str(i)  + str(i*2))
    j = 3
    while len(set(str(k))) == len(list(str(k))):
        if len(list(str(k))) == 9 and '0' not in list(str(k)):
            pandigital.append(k)
            break
        elif len(list(str(k))) > 9:
            break
        k = int(str(k) + (str(i*j)))
        j += 1
    
# return largest 1-9 pandigital
max(pandigital)
        
