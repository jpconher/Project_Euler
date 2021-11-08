# Problem 25

i = 3
previous = [1,1]
while True:
    F_i = sum(previous)
    if len(str(F_i)) >= 1000:
        break
    previous = [previous[-1],F_i]
    i += 1
    
    