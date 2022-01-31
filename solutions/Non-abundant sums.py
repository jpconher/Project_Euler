# Problem 23

# return factors of a number 
def factors(number):
    factors = [1]
    if number % 2 == 0: # even number
        for i in range(2,round(number/2)+1):
            if number % i == 0:
                factors.append(i)
    else: # odd number
        for i in range(3,round(number/2)+1,2):
            if number % i == 0:
                factors.append(i)   
    return factors 

upper_limit = 28123
abundant = []
for i in range(2,upper_limit+1): # upper bound is 28123
    if sum(factors(i)) > i:
        abundant.append(i)

numbers_written_abundant = set() # defined as set to avoid repeated numbers
for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
        if abundant[i]+abundant[j] > upper_limit: # numbers > upper_limit can be written as the sum of two abundant numbers
            break
        else:
            numbers_written_abundant.add(abundant[i]+abundant[j])
            
solution = [x for x in range(1,upper_limit+1) if x not in numbers_written_abundant]
print("""The sum of all positive integers that cannot be written as 
       the sum of two abundant numbers is""", sum(solution))
