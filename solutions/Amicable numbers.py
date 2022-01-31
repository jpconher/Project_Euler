# Problem 21

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

amicable = []
for i in range(1,10000):
    sum_factors = sum(factors(i))
    if i == sum(factors(sum_factors)) and i != sum_factors:
        amicable.append(i)
        
print("The sum of all amicable numbers under 10000 is", sum(amicable))

        
    
