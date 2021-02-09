# Problem 6

numbers = list(range(1,101))

# Analytical solution (more efficient than using function sum())
sum_squares = max(numbers)*(max(numbers)+1)*(2*max(numbers)+1)/6
square_sum = (max(numbers)*(max(numbers)+1)/2)**2

#difference
print(square_sum - sum_squares)
