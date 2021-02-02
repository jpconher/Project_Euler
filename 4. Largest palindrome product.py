# Problem 4

import numpy as np

def palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

candidates = sorted(set(np.concatenate(np.outer(list(range(101,1000)),list(range(101,1000))))), reverse=True)

for x in candidates:
    if palindrome(x):
        print("{:.0f} is the largest palindrome".format(x))
        break
    
#to obtain all palindromes
#palindromes = list((x for x in candidates if palindrome(x)))