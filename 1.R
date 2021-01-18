# problem 1

sum = 0
for (i in 3:999) {
  if (i %% 3 == 0 | i %% 5 == 0) {
    sum = sum + i
  }
}

# note that if we had to solve this same problem but for a larger set we would like
# to split it in two parts. Calculate the sum of the multiples of 3 and do the same
# for the multiples of 5.