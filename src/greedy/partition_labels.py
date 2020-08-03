def partitionLabels(S):
    """
    Find first and last occurrences for all and merge intervals
    Time: O(n) (note that the first_last_dict can have no more than 26 items)
    Space: O(1) first_last_dict has at most 26 items
    """

    # first_last_dict records the positions of first seen and last seen of a given char
    first_last_dict = {}
    for i in range(len(S)):
        if first_last_dict.get(S[i]) is None:
            # the first encounter of S[i], so i is the position of first seen and last seen
            first_last_dict[S[i]] = [i, i]
        else:
            # update the last seen position of S[i]
            first_last_dict[S[i]].pop()
            first_last_dict[S[i]].append(i)

    # once we have a first seen last seen dict,
    # we can treat the indices as intervals and then merge the overlapping intervals
    intervals = list(first_last_dict.values())
    intervals.sort(key=lambda x: x[0])
    # the following code can be found in merge_intervals.py
    partition_list = []
    for interval in intervals:
        if not partition_list or partition_list[-1][1] < interval[0]:
            partition_list.append(interval)
        else:
            partition_list[-1][1] = max(partition_list[-1][1], interval[1])

    res = []
    for p in partition_list:
        res.append(p[1] - p[0] + 1)

    return res


def partitionLabels_greedy(S):
    """
    Greedy
    Time: O(n)
    Space: O(1) last_seen has most 26 items
    """
    # last_seen only records the positions of last seen
    last_seen = {c: i for i, c in enumerate(S)}

    # start denotes the starting position of a new partition
    j = start = 0

    ans = []
    for i, c in enumerate(S):
        j = max(j, last_seen[c])
        # if i is the same as j:
        # all the previous last_seen has been included between start and j
        if i == j:
            ans.append(i - start + 1)
            start = i + 1

    return ans


test = "ababcbacadefegdehijhklij"
print(partitionLabels(test))
