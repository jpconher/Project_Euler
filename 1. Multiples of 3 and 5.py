import time

start_time = time.time()

sum_multiples = 0
for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum_multiples += i

print("{:.5f}".format(time.time() - start_time))
