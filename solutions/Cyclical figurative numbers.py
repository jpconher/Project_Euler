# Problem 61

from itertools import permutations

def is_valid_combination(c, prefixes):
    # check that combination is valid
    return ((len(set(c)) == len(c)) and 
            (len(set([prefixes[x][i] for i in range(2) for x in c])) <= 6))
         
def polygonal(n, type = "Triangle"):
    # computes P_n_ for type specified
    if type == "Triangle":
        return int(n*(n + 1)/2)
    elif type == "Square":
        return int(n**2)
    elif type == "Pentagonal":
        return int(n*(3*n - 1)/2)
    elif type == "Hexagonal":
        return int(n*(2*n - 1))
    elif type == "Heptagonal":
        return int(n*(5*n - 3)/2)
    else: # type octogonal
        return int(n*(3*n - 2))

types = ["Triangle", "Square", "Pentagonal", "Hexagonal", 
         "Heptagonal", "Octogonal"]
polygonal_numbers = {}
prefixes = {}
result = []
while not result:
    # get all 4-digits polygonal numbers
    for t in types:
        i = 1
        polygonal_numbers[t] = []
        while True:
            p_n = polygonal(i, t) 
            if len(str(p_n)) == 4 and str(p_n)[2] != '0': # 3rd-digit cannot be 0
                prefixes[p_n] = [int(str(p_n)[:2]), int(str(p_n)[2:])]
                polygonal_numbers[t].append(polygonal(i, t))
            elif len(str(p_n)) > 4:
                break
            i += 1
    for o in polygonal_numbers['Octogonal']:
        for h in polygonal_numbers['Heptagonal']:
            for hexa in polygonal_numbers['Hexagonal']:
                for p in polygonal_numbers['Pentagonal']:
                    if not is_valid_combination([o, h, hexa, p], prefixes):
                        continue
                    for s in polygonal_numbers["Square"]:
                        if not is_valid_combination([o, h, hexa, p, s], prefixes):
                            continue
                        for t in polygonal_numbers["Triangle"]:
                            if not is_valid_combination([o, h, hexa, p, s, t], prefixes):
                                continue
                            else:
                                for per in permutations([o, h, hexa, p, s, t], 6):
                                    if all(str(per[i-1])[-2:] == str(per[i])[:2] for
                                           i in range(0,len(per))):
                                        result = per
                                        break
                            if result:
                                break
                        if result:
                            break
                    if result:
                        break
                if result:
                    break
            if result:
                break
        if result:
            break