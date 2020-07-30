def prisonAfterNDays(cells, N):
    """
    Update for each day
    Time: O(NC) C - number of cells
    Space: O(C)
    """
    if N == 0:
        return cells
    for day in range(N):
        next_cell = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            next_cell[i] = int(cells[i - 1] == cells[i + 1])
        cells = next_cell
    return cells


def prisonAfterNDays_cycle(cells, N):
    """
    Update for each day with cycle (once we are in a cycle, the update will be the same)
    Time: min(O(TC), O(NC)) T - length of a period, if a period contains all possible states of cells (worst case)
    then the period length would be 2^C. If N is small, then this method is roughly the same as the first method.
    If N is large, then this method is significantly faster

    Space: min(O(TC), O(NC)) cycle and all comb
    """
    # when len(cells) = 8, the period length is 14
    # all_comb to store all seen combinations, if we reached a comb that had been seen already, we are in a loop
    all_comb = set()
    cycle = {}
    if N == 0:
        return cells
    for day in range(1, N + 1):
        next_cell = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            next_cell[i] = int(cells[i - 1] == cells[i + 1])
        cells = next_cell
        # list is unhashable, so use tuple instead
        if tuple(next_cell) not in all_comb:
            cycle[day] = next_cell
            all_comb.add(tuple(next_cell))
        # we have gathered all possible state in a cycle, break
        else:
            break
    if N % len(cycle) == 0:
        return cycle[len(cycle)]
    return cycle[N % len(cycle)]


test = [0, 1, 0, 1, 1, 0, 0, 1]
test_n = 7

print(prisonAfterNDays(test, test_n))
print(prisonAfterNDays_cycle(test, test_n))
