# Problem 42

import pandas as pd

def is_triangle_word(word,triangle_numbers):
    equivalence = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
                   "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,
                   "R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,
                   "Z":26}
    if sum([equivalence[letter] for letter in word]) in triangle_numbers:
        return True
    else:
        return False
        
# import .txt file
word_list = pd.read_csv('Downloads\p042_words.txt', header = None, delimiter = ",", dtype=str)

# get largest word
max_letters = max([len(word) for word in word_list.iloc[0]])

# at most, the letters in a word can sum up to 14*26 = 364. Obtain triangle numbers <= to that number
triangle_numbers = [1]
n = 2
while triangle_numbers[-1] <= max_letters*26:
    triangle_numbers.append(int(1/2*n*(n+1)))
    n += 1
triangle_numbers.pop() # get rid of last number since > than maximum

triangle_words = []
for word in word_list.iloc[0]:
    if is_triangle_word(word,triangle_numbers):
        triangle_words.append(word)
        
        
    