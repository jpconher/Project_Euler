# Problem 14

number_len_seq = {}
for i in range(1,1000000):
    s = 1
    j = i
    while j>1:
        if number_len_seq.get(j):
            s = s + number_len_seq[j] - 1 
            break 
        if j%2==0:
            j = j/2
        else:
            j = 3*j+1
        s += 1
    number_len_seq[i] = s
    
print("The number with the longest chain:", max(number_len_seq, 
                                                   key=number_len_seq.get))

