from collections import deque


def numSquares_dp(n):
    """
    Dynamic programming (slow, time limit exceeded)
    Time: O(n*sqrt(n))
    Space: O(n)
    """
    from collections import defaultdict
    dp = defaultdict(int)
    # total time: int(sqrt(1)) + int(sqrt(2)) + ... + int(sqrt(n))
    # there will be (i+1)^2 - i^2 = 2i-1 repeating numbers between sqrt((i+1)^2) and sqrt(i^2)
    # The predominant term in the sum above is n*int(sqrt(n)), therefore O(n*sqrt(n))
    for i in range(1, n+1):
        # loop for n times
        dp[i] = i
        j = 1
        while i - j ** 2 >= 0:
            # loop for int(sqrt(i)) times, for every i
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1
    return dp[n]


def numSquares(n):
    """
    Brute force recursion (slow, time limit exceeded)
    """
    i = 2
    sq_list = []
    while i**2 <= n:
        sq_list.append(i**2)

        if i**2 == n:
            return 1

        i += 1

    return sum_in_list(n, sq_list)


def sum_in_list(summ, l):
    sublist = [i for i in l if i <= summ]
    min_num = summ
    if len(sublist) == 0:
        return summ
    for i in range(len(sublist)-1, -1, -1):
        curr_divide = sublist[i]
        excess = summ % curr_divide
        if 0 < excess < 4:
            new_len = excess + int(summ/curr_divide)
        elif excess == 0:
            new_len = int(summ/curr_divide)
        else:
            new_len = sum_in_list(excess, sublist[:-1]) + int(summ/curr_divide)
        if new_len < min_num:
            min_num = new_len
    return min_num


def numSquare_BFS(n):
    """
    Breadth First Search (fast)
    Time: ?
    Space: O(n) (constant multiple of n: q, v and curr_chile in each while loop)
    """
    #             12
    #      /   |        \
    #     3    8         11
    #    /    / \       / |   \
    #   2    4   7     2  7    10
    #  /   / \   /\   /   /\  / | \
    # 1  *0*   3 3  6 1   3 6  1 6  9
    # ...
    # set the root and initialise the queue
    # the second number in the tuple stores the number of edges between a node and the root
    root = (n, 0)
    q = deque()
    q.append(root)
    # set of visited nodes
    v = {n}

    # loop if q is not empty
    while q:
        # dequeue the node and get all its neighbours (children)
        curr_node = q.popleft()
        curr_child = [curr_node[0] - i ** 2 for i in range(1, int(curr_node[0] ** 0.5) + 1)]
        for c in curr_child:
            # stop if the first 0 is reached, return the number of edges between the root and that 0
            # the path from the root to this 0 will be the shortest, since BFS is scanning layer by layer
            if c == 0:
                return curr_node[1] + 1
            # if c not visited before, enqueue c and add it to the visited nodes
            # if c is already in visited nodes, that means the current c's children will lead to a solution
            # no better than the previously visited c, therefore one can stop searching for the current c's children

            # Alternatively, transform the tree into a graph and merge all the nodes with the same values, then the
            # question becomes to find the shortest path between node n and node 0, which can be solved using BFS
            # BFS will visit ALL the nodes in one hop away, the two hops and so on, the hop counts when one sees
            # the first occurrence of 0 will be the length of the shortest path
            elif c not in v:
                q.append((c, curr_node[1]+1))
                v.add(c)

