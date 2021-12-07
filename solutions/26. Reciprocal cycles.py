# Problem 26

# considering only prime divisors would speed up the algorithm.

def length_recurring_cycle(d):
    remainder = 1
    while remainder < d:
        remainder = remainder*10
    remainder = [remainder]
    while len(set(remainder)) == len(remainder):
        if remainder[-1] > d:
            remainder.append(10*(remainder[-1]-divmod(remainder[-1]/d,1)[0]*d))
        if remainder[-1] < d:
            remainder.append(10*remainder[-1])
        if remainder[-1] == d:
            return(0)
    indices = [i for i, x in enumerate(remainder) if x == remainder[-1]]
    return(indices[-1]-indices[0])
    
length = 0    
for d in range(1,1001):
    if length < length_recurring_cycle(d):
        length = length_recurring_cycle(d)
        number = d


