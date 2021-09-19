# Problem 22

# load data
f = open('p022_names.txt', 'r')

# store data in variable 'names' and sort
names = f.read().split(",")
names.sort()

total_score = 0
for position in range(0,len(names)):
    name_score = 0
    for letter in names[position]:
        if letter != '"':
            name_score += ord(letter) - 64 # capital letters (ord("A")=65, ord("B")=66,...)
    total_score += name_score * (position+1)

    
        
