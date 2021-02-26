# Problem 14

number_len = {1:1}
for i in range(2,1000000):
    s = 1
    j = i
    while j>1:
        if j%2==0:    
            j = j/2
            s += 1
            if number_len.get(j):
                number_len[i] = s + number_len[j]
                break 
        else:
            j = 3*j+1
    
print("The number with the longest chain:", max(number_len, 
                                                   key=number_len.get))

