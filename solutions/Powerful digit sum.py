# Problem 56

def digits_sum(n):
    return sum([int(d) for d in list(str(n))])

maximum_sum = 0
b = 99
while b > 0:
    for a in range(99,0,-1):
        candidate = a**b
        if a % 10 == 0: # the last digit in a cannot be 0
            continue
        elif maximum_sum > 9*len(list(str(candidate))):
            break
        elif digits_sum(candidate) > maximum_sum:
            maximum_sum = digits_sum(candidate)
    b -= 1