from collections import deque
from copy import deepcopy
from itertools import chain


def orangesRotting(grid):
    """
    Find all rotten and update at every step
    """
    def one_step_bfs(rotten_list, grid_old):
        grid = deepcopy(grid_old)
        grid_len = len(grid)
        grid_wid = len(grid[0])

        while len(rotten_list) > 0:
            node_i, node_j = rotten_list.pop()

            # up
            if node_i > 0 and grid[node_i - 1][node_j] == 1:
                grid[node_i - 1][node_j] = 2
            # left
            if node_j > 0 and grid[node_i][node_j - 1] == 1:
                grid[node_i][node_j - 1] = 2
            # down
            if node_i < grid_len - 1 and grid[node_i + 1][node_j] == 1:
                grid[node_i + 1][node_j] = 2
            # right
            if node_j < grid_wid - 1 and grid[node_i][node_j + 1] == 1:
                grid[node_i][node_j + 1] = 2
        return grid

    if 2 not in set(chain.from_iterable(grid)):
        if 1 in set(chain.from_iterable(grid)):
            return -1
        else:
            return 0
    minute = 0
    rotten = []
    while True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
        new_grid = one_step_bfs(rotten, grid)

        if new_grid != grid:
            minute += 1
        else:
            break
        grid = new_grid.copy()
        del new_grid
    if 1 in set(chain.from_iterable(grid)):
        minute = -1

    return minute


def orangesRotting_bfs(grid):
    """
    BFS, with stopping sign
    Time: O(m*n), m: length of grid, n: width of grid
    Space: O(n) (of the queue, worst case: full of rotten oranges)
    """
    # track number of fresh oranges, to determine whether output -1 or not
    not_rotten = 0
    # minute start with -1 since it will be incremented before any propagation
    minute = -1
    queue = deque()
    grid_len = len(grid)
    grid_wid = len(grid[0])

    # O(m*n)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                # all the source of propagation
                queue.append((i, j))
            if grid[i][j] == 1:
                # existing fresh oranges
                not_rotten += 1
    # this is the stopping sign, meaning we have completed one round of update
    # using queue is necessary here because this will be popped out last (after all the existing rotten oranges)
    queue.append((-1, -1))

    # O(m*n), worst case will traverse all the cells
    while queue:
        row, col = queue.popleft()
        # one round of update has been completed
        if row == -1:
            minute += 1
            # if remove checking empty, will adding (-1, -1) forever
            if queue:
                # add the stopping sign of the new round,
                # which will be popped after all the rest in the queue have been popped out
                queue.append((-1, -1))

        # during one round of update, only update the immediate neighbours
        else:
            # up
            if row > 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                not_rotten -= 1
                queue.append((row - 1, col))
            # left
            if col > 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                not_rotten -= 1
                queue.append((row, col - 1))
            # down
            if row < grid_len - 1 and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                not_rotten -= 1
                queue.append((row + 1, col))
            # right
            if col < grid_wid - 1 and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                not_rotten -= 1
                queue.append((row, col + 1))

    # if towards the end there are still fresh oranges
    if not_rotten > 0:
        return -1
    # otherwise all oranges are rotten
    else:
        return minute


test1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
test2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting_bfs(test1))
print(orangesRotting_bfs(test2))
