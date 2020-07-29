def eraseOverlapIntervals(intervals):
    """
    Greedy with sorting (prefer smaller right bounds)
    Time: O(nlogn)
    Space: O(1)
    """
    intervals.sort()

    res = 0
    # last is the index of the last non-deleted interval
    last = 0

    for i in range(1, len(intervals)):

        if intervals[i][0] == intervals[last][0]:
            # after sorting, choose the one with smaller right boundary to keep, remove the others
            res += 1

        elif intervals[i][1] < intervals[last][1]:
            # in this case the current interval is contained in the last non-deleted interval
            # since we prefer smaller right bounds,
            # we remove the larger interval and update the last non-deleted interval as the current interval
            res += 1
            last = i

        elif intervals[i][0] < intervals[last][1]:
            # in this case we have something like [2, 5] and [3, 7], remove the latter
            res += 1

        else:
            # in this case there is no overlapping, advance the remained intervals by one
            last = i

    return res


test = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(eraseOverlapIntervals(test))
