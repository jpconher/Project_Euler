# Problem 24

digits = [0,1,2,3,4,5,6,7,8,9]

i = 0
while i < 999999:
    for j in range(9,-1,-1):
        if digits[j] > digits[j-1]:
            x = digits[j-1:]
            if len(x) == 2:
                digits[j-1:] = sorted(x, reverse = True)
            else:
                if digits[j-1] > min(x[1:]):
                    digits[j-1] = x.pop(x.index(min([i for i in x if i > digits[j-1]])))
                else:
                    digits[j-1] = x.pop(x.index(min(x[1:])))
                digits[j:] = sorted(x)
            break
    i += 1
