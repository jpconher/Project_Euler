# Problem 63

from math import ceil

result = []
exponent = 1
while True:
    base = ceil(10**((exponent - 1)/(exponent)))
    if len(str(base**exponent)) > exponent:
        break
    else:
        while len(str(base**exponent)) <= exponent:
            result.append(base**exponent)
            base += 1
        exponent += 1
    