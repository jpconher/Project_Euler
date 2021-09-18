# Problem 21

# return factors of a number 
def factors(number):
    factors = [1]
    for i in range(2,round(number/2)+1):
        if number % i == 0:
            factors.append(i)
    return factors 

amicable = [] # 1 is an amicable number
for i in range(1,10000):
    sum_factors = sum(factors(i))
    if i == sum(factors(sum_factors)) and i != sum_factors:
        amicable.append(i)
        
print("The sum of all amicable numbers under 10000 is", sum(amicable))
        
    
