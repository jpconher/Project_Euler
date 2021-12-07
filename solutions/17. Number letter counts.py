# Problem 17

# create dictionary with equivalences
equivalences = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
                7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
                12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
                16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
                20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
                70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred",
                1000:"thousand"}

sum_letters = 0
for i in range(1,1001):
    a = sum_letters
    if i < 21: # 1, 2, 3, ..., 20
        sum_letters += len(equivalences.get(i))     
    elif i % 10 == 0:
        if i < 91: # 30, 40, 50, ..., 90
            sum_letters += len(equivalences.get(i))
        elif i == 1000:
            sum_letters += len(equivalences.get(i/1000)) + len(equivalences.get(1000)) 
        elif i % 100 == 0: # 100, 200, 300, ..., 
            sum_letters += len(equivalences.get(i/100)) + len(equivalences.get(100)) 
        else: # 110, 120, ..., 210, 220, ..., 980, 990
            digits = [int(d) for d in str(i)]
            sum_letters += len(equivalences.get(digits[0])) + len(equivalences.get(100)) + \
                len("and") + len(equivalences.get(digits[1]*10)) 
    elif i < 100: # 21, 22, ..., 29, 31, 32, ..., 98, 99
        digits = [int(d) for d in str(i)]
        sum_letters += len(equivalences.get(digits[0]*10)) + len(equivalences.get(digits[1]))
    else: # 101, 102, 109, 111, 112, ..., 998
        digits = [int(d) for d in str(i)]
        if digits[1] != 0:
            if digits[1] == 1: # treat 11-19 separately 
                sum_letters += len(equivalences.get(digits[0])) + len(equivalences.get(100)) + \
                    len("and") + len(equivalences.get(int(str(digits[1]) + str(digits[2]))))
            else:
                sum_letters += len(equivalences.get(digits[0])) + len(equivalences.get(100)) + \
                    len("and") + len(equivalences.get(digits[1]*10)) + len(equivalences.get(digits[2]))
        else:
            sum_letters += len(equivalences.get(digits[0])) + len(equivalences.get(100)) + \
                len("and") + len(equivalences.get(digits[2]))

# notice that the code could be simplified using functions. Furthermore, it can
# potentially be generalised to handle numbers greater than 1000. 
