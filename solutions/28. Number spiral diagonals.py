# Problem 28

# It is easy to see the patterns in the diagonals:
    # upper right diagonal: i-th element given by {(2*i+1)^2} = {9,25,49,...}
    # upper left diagonal: i-th element given by {((2*i+1)^2-2*i)} = {7,21,43,...}
    # lower right diagonal: i-th element given by {(2*i)^2+1-2*i} = {3,13,31,...}
    # lower left diagonal: i-th element given by {(2*i)^2+1} = {5,17,37,...}
    
upper_right = []
upper_left = []
lower_right = []
lower_left = []

dimension = 1001

for i in range(1,int((dimension-1)/2)+1):
    upper_right.append((2*i+1)**2)
    upper_left.append(upper_right[-1]-2*i)
    lower_right.append((2*i)**2+1-2*i)
    lower_left.append(lower_right[-1]+2*i)
    
sum_diagonals = sum(upper_right+upper_left+lower_right+lower_left) + 1
