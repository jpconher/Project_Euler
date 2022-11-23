# Problem 44

def pentagonal(n):
    return int(n*(3*n-1)/2)

def natural_solution(k):
    if ((1 + (1+24*k)**0.5)/6).is_integer():
        return True
    else:
        return False
    
pentagonal_list = [1]
n = 1
diff = 0
while True:
    pentagonal_list.append(pentagonal(n+1))
    if diff > 0 and pentagonal_list[-1] - pentagonal_list[-2] > diff:
        break
    for i in range(1,n+1):
        if diff > 0 and pentagonal_list[-1]-pentagonal_list[-1-i] > diff:
            break
        elif (natural_solution(pentagonal_list[-1]-pentagonal_list[-1-i]) and 
              natural_solution(pentagonal_list[-1]+pentagonal_list[-1-i])):
            diff = pentagonal_list[-1]-pentagonal_list[-1-i]
    n += 1

        




