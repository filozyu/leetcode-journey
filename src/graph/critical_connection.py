# DFS, Bridge in a graph, articulation point, connected graphs, detecting loops using DFS tree
from collections import defaultdict


def criticalConnections(n, connections):
    """
    Time Limit Exceeded
    Brute Force (remove each edge and see if the resulting graph is connected)
    Time: O(E * (V+E)) for DFS or BFS (not considering the time for constructing the adjacency list)
    Space: O(E + 2E + V + V)
    the first E is the copy of connections,
    2E+V is the adj list created by construct_undirected_graph
    the last V is visited
    """
    # any edge not in a loop is a critical connection
    if len(connections) == 1:
        return connections
    critical = []
    for i in range(len(connections)):
        all_edges = connections.copy()
        curr_edge = all_edges.pop(i)
        new_num_nodes = dfs_graph(all_edges)
        if new_num_nodes < n:
            critical.append(curr_edge)
        del all_edges
    return critical


def dfs_graph(all_edges):
    """
    Construct adjacency list using all_edges and then perform DFS on the graph
    """
    adj_list = defaultdict(list)
    for e in all_edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])
    root = all_edges[0][0]
    visited = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.append(curr_node)
        else:
            continue
        neighbours = adj_list[curr_node]
        stack += neighbours
    return len(visited)


def criticalConnections_fast(n, connections):
    """
    DFS with searching loops (via back edges)
    Time: O(V + E) (Time complexity of DFS)
    Space: O(V) (not considering the adjacency list)
    """

    def dfs_trace(v):
        """
        Three cases when we encounter node v as we go down the DFS tree,
        suppose we are at node p and node v is one of p's neighbours
        (not necessarily adding v to the tree)

        1. v has not been visited before -> add v to the tree
        2. v has been visited before, it is p's parent -> do not add v to the tree
        3. v has been visited before, it is p's ancestor (not direct parent) -> do not add v to the tree

        (dfs_trace is only called upon in the first case)
        """
        # count is an int and it's from outer scope so we need to declare it here
        nonlocal count  # denotes the order of node v when it is added in the DFS tree

        # visited[v] denotes whether or not v is in the tree
        visited[v] = True

        # discover[v] denotes the order of v when it is added in the DFS tree (not the tree level)
        discover[v] = count

        # low[v] denotes the earliest node (earliest added to the tree) in the tree that
        # we can reach via back edges in the subtree rooted at v (v's parent is not included)
        # (the back edges are not in the real tree)
        low[v] = count

        # increment the order for the next node to be added in the tree
        count += 1

        # e.g. connections: [[0, 1], [1, 2], [2, 0], [1, 3]]
        #   0 - 1 - 3
        #   | /
        #   2

        # 2 examples of DFS tree (left: root 0, right: root 1)
        #   0     |   1
        #   |     |   | \
        #   1     |   0  3
        #   | \   |   |
        #   2  3  |   2

        # left: discover = [0, 1, 2, 3] (0 -> 1 -> 2 -> 3)
        # right: discover = [1, 0, 2, 3] (1 -> 0 -> 2 -> 3)

        # left: low = [0, 0, 0, 3] (1 through 2 to 0, 2 directly to 0, 3 last visited and has no back edge)
        # right: low = [0, 0, 0, 3] (0 through 2 to 1 , 2 directly to 1, 3 last visited and has no back edge)

        # A pair (u, v) is a critical edge if:
        # 1) it is an edge in the tree, suppose u is the parent of v;
        # 2) low[v] > discover[u].

        # Since then v has no other path in the graph to u, the edge we have in the tree is the sole connection

        # Recur for all the vertices adjacent to this vertex
        for c in adj_list[v]:
            # If c is not visited yet, then it is a child of v in the tree
            if visited[c] is False:
                parent[c] = v
                dfs_trace(c)
                # since c is in the subtree rooted at v, any previous nodes that can be visited by c via back edges
                # can also be visited by v, low[v] should be at least low[c]
                low[v] = min(low[v], low[c])
                # This is when (v, c) as an edge in the tree, is also the sole path between v and c in the graph
                # this means c can only be visited from v
                if low[c] > discover[v]:
                    res.append([v, c])

            # if we have already visited c before v and c is not v's parent, then we have a back edge from v to c
            elif c != parent[v]:
                # low[v] is now at lest discover[c], the order of c when it was added (before v)
                low[v] = min(low[v], discover[c])

    # res contains all the critical edges
    res = []
    # The first node (i.e. the root of the DFS tree) will have order 0
    count = 0
    # construct adjacency list
    adj_list = defaultdict(list)
    for e in connections:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])

    # initialise the arrays
    visited = [False] * n
    discover = [float("Inf")] * n
    low = [float("Inf")] * n
    parent = [-1] * n

    # if the graph is connected, then we don't need to run the for loop
    # dfs_trace(connections[0][0])

    # this for loop is necessary for graphs that are not connected
    for i in range(n):
        if visited[i] is False:
            dfs_trace(i)

    return res


test_E = 4
test = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(criticalConnections_fast(test_E, test))
