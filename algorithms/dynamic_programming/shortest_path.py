import time
import numpy as np

def shortest_path_brute_force(curr_row, curr_column, grid):
    if curr_row >= len(grid) or curr_column >= len(grid[0]):
        return float("inf")
    elif curr_row == len(grid)-1 and curr_column == len(grid[0])-1:
        return 0
    down = shortest_path_brute_force(curr_row+1, curr_column, grid)
    right = shortest_path_brute_force(curr_row, curr_column+1, grid)
    return min(down, right)+1

def shortest_path_dynamic_programming(grid):
    grid[:, -1] = np.arange(len(grid))[::-1]
    grid[-1, :] = np.arange(len(grid[0]))[::-1]
    for row in reversed(range(len(grid)-1)):
        for column in reversed(range(len(grid[0])-1)):
            grid[row, column] = min(grid[row+1, column], grid[row, column+1])+1
    print(grid)
    return grid[0,0]

grid = np.zeros((10,10), dtype=int)

start = time.time()
shortest_path_dp = shortest_path_dynamic_programming(grid=grid)
dp_time = time.time() - start
print(dp_time, shortest_path_dp)

start = time.time()
shortest_path_bf = shortest_path_brute_force(curr_row=0, curr_column=0, grid=grid)
bf_time = time.time() - start
print(bf_time, shortest_path_bf)