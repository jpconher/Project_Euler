# Problem 30

# power
p = 5

numbers = []
i = 2
while i < 9**5*len(str(i)):
    if sum(int(d)**p for d in str(i)) == i:
        numbers.append(i)
        i += 1
    elif sum(int(d)**p for d in str(i)) < i:
        i += 1
    else:
        digits = list((int(d) for d in str(i)))
        for j in range(0,len(digits)):
            if digits[j]**p > i:
                if j == 0:
                    i = 10**len(str(i))
                    break
                else:
                    digits[j-1] += 1
                    digits[j:] = [0]*(len(digits)-j)
                    i = str()
                    for k in digits:
                        i += str(k)
                    i = int(i)
                    break
            if j == len(digits)-1:
                i += 10-digits[j]