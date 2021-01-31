# Problem 2

def generate_fibonacci(limit):
    if limit == 1:
        series = [1]
    else:
        series = [1,2]
    while series[-1] < limit:
        series.append(series[-1]+series[-2])
    return series[:-1]

def sum_even(numbers):
    sum = 0
    for i in numbers:
        if i%2 == 0:
            sum += i
    return sum

sum_even_fibonacci = sum_even(generate_fibonacci(4000000))