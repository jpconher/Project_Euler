# Problem 48
     
series = 0
for n in range(1,1000):
    if n % 10 != 0:
        series += n**n

print(str(series)[-10:])
