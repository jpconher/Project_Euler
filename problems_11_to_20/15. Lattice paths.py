# Problem 15

import numpy as np

dimension = 21 # dimension + 1 (stores the borders as cells)

# create matrix dimension-by-dimension
grid = np.zeros((dimension, dimension))

# assign to each cell the number of possible paths 
for i in range(0,dimension):
    grid[0,i] = 1
    grid[i,0] = 1

for i in range(1,dimension):
    for j in range(1,dimension):
        grid[i,j] = int(grid[i-1,j] + grid[i,j-1])
        
print("The number of possible paths for a " + str(dimension) + "x" + str(dimension)
      + " grid is", int(grid[dimension-1,dimension-1]))