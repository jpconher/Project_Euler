# Problem 32 

# check that product is pandigital
def pandigital(multiplicand,multiplier,product):
    if multiplicand * multiplier == product:
        digits = list(range(1,10))
        n = str(multiplicand)+str(multiplier)+str(product)
        for x in n[0:len(n):1]:
            if int(x) in digits:
                digits.pop(digits.index(int(x)))
            else:
                return 0
        return 1
    else:
        return "Identity is incorrect."
    
# pandigital products
n = []
    
run = True
while run:
    for multiplicand in range(1,5001,1):
        for multiplier in range(1,10000,1):
            if len(str(multiplicand*multiplier)+str(multiplicand)+str(multiplier)) == 9:
                if pandigital(multiplicand,multiplier,multiplicand*multiplier) == 1:
                    n.append(multiplicand*multiplier)
            elif len(str(multiplicand*multiplier)+str(multiplicand)+str(multiplier)) > 9:
                break
    if multiplicand == 5000:
        run = False
    
print(sum(set(n)))        
                
                
            

    
