def findContentChildren(g, s):
    """
    Greedy with sorting (always TRY to assign the current smallest cookie to the least greedy child)
    Time: O(glogg + slogs)
    Space: O(1)
    """
    g.sort()
    s.sort()

    res = 0
    # curr_g and curr_s denote the position in g and s
    curr_g, curr_s = 0, 0

    while curr_g < len(g) and curr_s < len(s):
        # if the current cookie (smallest possible) can satisfy the current child (least greedy)
        if s[curr_s] >= g[curr_g]:
            # move to the next cookie and the next child
            curr_s += 1
            curr_g += 1
            res += 1
        # otherwise the current cookie cannot satisfy the least greedy child, so it cannot satisfy any other child
        # try next cookie
        else:
            curr_s += 1

    return res


test_g, test_s = [1, 2, 3], [1, 1]
print(findContentChildren(test_g, test_s))
