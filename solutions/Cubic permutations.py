# Problem 62

def cube(n):
    return n**3

candidates = {}
i = 1
while True:
    cubic_number = cube(i)
    cubic_number_digits = tuple(sorted(list(str(cubic_number))))
    if cubic_number_digits not in candidates.keys():
        candidates[cubic_number_digits] = [cubic_number]
    else:
        candidates[cubic_number_digits].append(cubic_number)
    if len(candidates[cubic_number_digits]) == 5:
        print(min(candidates[cubic_number_digits]))
        break
    i += 1
    

