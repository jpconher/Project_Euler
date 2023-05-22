# Problem 52

i = 1
j = 6
while j > 1:
    j = 6
    while sorted(str(i)) == sorted(str(i*j)):
        j += -1
        if j == 1:
            print(i)
    # if the number of digits in 6*i is larger than i then consider 
    # number with one more digit
    if 6*i > 10**len(str(i)):
        i = 10**len(str(i))
    else:
        i += 1
        
            
        

