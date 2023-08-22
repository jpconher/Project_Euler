# Problem 68

""" note: 16-digits strings are formed when 10 is located in the outer nodes. 
When 10 is in an inner node 17-digits strings are formed. """

from itertools import permutations

# get all possible combinations with 10 in outer nodes
candidates = [a for a in permutations(range(1, 11), 10) if 10 not in a[:5]]

solution = 0
for c in candidates:
    # get inner and outer nodes
    inner_nodes = c[0:5]
    outer_nodes = c[5:11]
    # get lowest outer node
    lowest_outer_index = outer_nodes.index(min(outer_nodes))
    # get candidate starting from lowest outer index
    c_str = ""
    line_sum = [0, 0]
    for i in range(lowest_outer_index, lowest_outer_index + 5):
        c_str += f"{outer_nodes[i % 5]}{inner_nodes[i % 5]}{inner_nodes[(i + 1) % 5]}"
        line_sum[1] = outer_nodes[i % 5] + inner_nodes[i % 5] + inner_nodes[(i + 1) % 5]
        if (line_sum[0] == 0) | (line_sum[0] == line_sum[1]):
            line_sum[0] = line_sum[1]
        else:
            break
    # check if candidate is larger than existing solution
    if int(c_str) > solution:
        solution = int(c_str)

print(solution)
