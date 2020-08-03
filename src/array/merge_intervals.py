def merge(intervals):
    """
    Iteratively merge with the current interval with the smallest upper bound
    Time: O(n^2) in the worst case all intervals are disjoint, popping the first entry of a list is O(n)
    Space: O(1) (return not included)
    """
    merged = []
    # sort intervals by upper bounds
    intervals.sort(key=lambda x: x[1])
    while intervals:
        init_interval = intervals.pop(0)
        i = 0
        while True:
            # in this while loop, find all intervals that overlap with init_interval and merge them
            if i == len(intervals):
                break
            if intervals[i][0] <= init_interval[1] <= intervals[i][1]:
                # merge init_interval with intervals[i]
                init_interval = [min(intervals[i][0], init_interval[0]), intervals[i][1]]
                # remove the merged interval
                intervals.pop(i)
                # reset i
                i = 0
            elif intervals[i][0] > init_interval[0] and intervals[i][1] < init_interval[1]:
                # in this case intervals[i] is completely included in init_interval
                # remove it
                intervals.pop(i)
                # reset i
                i = 0
            else:
                # otherwise we intervals[i] is disjoint with init_interval, move to the next interval
                # this disjoint interval will be dealt with in future while loops (when it is popped out)
                i += 1
        # append the merged interval
        merged.append(init_interval)

    return merged


def merge_interval_fast(intervals):
    """
    Sort intervals by lower bounds
    Time: O(nlogn)
    Space: O(1) (return not included)
    """
    # sort the intervals by lower bounds
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:

        if not merged or merged[-1][1] < interval[0]:
            # in this case either interval is the first one or it is disjoint with the previous one
            merged.append(interval)
        else:
            # merge the current interval withe the last one in the merged
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


test = [[1, 3], [4, 6], [8, 10], [15, 18]]
print(merge(test))
