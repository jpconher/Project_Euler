# Problem 74

import math

def digits_factorial(n:int) -> int:
    ''' Compute the sum of the factorials of the digits of n '''
    return sum(math.factorial(int(d)) for d in list(str(n)))

def non_repeating_terms(n:int, chains:dict) -> list:
    ''' Compute the chain of non-repeating terms of the factorials of the 
    digits of n. The terms included in the dictionary chains are excluded 
    since their length until repetition is known. '''
    terms = [n]
    while True:
        terms.append(digits_factorial(terms[-1]))
        if terms[-1] in chains.keys():
            return(terms) 
        elif terms[-1] in terms[:-1]:
            return(terms[:-1])
    
# upper bound
n = 10**6

# store results to speed up code
chains = {}

for i in range(1, n + 1):
    if i not in chains.keys():
        # get non-repeating terms
        terms = non_repeating_terms(i, chains)
        # the chain length of one of the intermediate terms is known
        if terms[-1] in chains.keys():
            for j in range(0, len(terms) - 1):
                chains[terms[j]] = (len(terms) - j) + (chains[terms[-1]] - 1)
        # the chain length of the intermediate terms is unknown
        else:
            for j in range(0, len(terms)):
                chains[terms[j]] = len(terms) - j

            
# check chains with exactly 60 non-repeating terms
solution = sum(1 for value in chains.values() if value == 60)
