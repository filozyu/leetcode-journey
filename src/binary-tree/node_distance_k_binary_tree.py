# BFS, binary tree, distance from a node

from utils import list2binary_tree

from collections import defaultdict, deque


def BFS(root, neighbour_dict, K):
    """
    BFS on a graph (adjacent list), return all nodes with distance K from the root
    Time: O(2^K) number of nodes need to check (from root to layer K) the sum is 2^(K+1) = 2 * 2^K
    Space: O(n) visited and queue
    """
    res = []
    visited = set()
    q = deque()
    depth = 0
    # root has to be an int
    q.append((root, depth))
    while q:
        curr_pair = q.popleft()
        visited.add(curr_pair[0])
        curr_depth = curr_pair[1]
        if curr_depth == K:
            res.append(curr_pair[0])
        for n in neighbour_dict[curr_pair[0]]:
            if n not in visited:
                # here we have reached the next layer
                q.append((n, curr_depth + 1))
    return res


def distanceK(root, target, K):
    """
    Make target the new root then run BFS on the new graph
    Time: O(n) Construction of the adj dict (longer) and BFS
    Space: O(n) n - number of nodes; the adjacency dict has the size of 2*E, E = n - 1, the number of edges
    """
    # Note that here every node has a unique value
    # target should be an int, if it's a TreeNode, input target.val in BFS
    queue = deque()
    neighbour_dict = defaultdict(list)
    queue.append(root)
    while queue:
        curr_node = queue.popleft()
        if curr_node is not None:
            if curr_node.left is not None:
                neighbour_dict[curr_node.val].append(curr_node.left.val)
                neighbour_dict[curr_node.left.val].append(curr_node.val)
            if curr_node.right is not None:
                neighbour_dict[curr_node.val].append(curr_node.right.val)
                neighbour_dict[curr_node.right.val].append(curr_node.val)
            queue.append(curr_node.left)
            queue.append(curr_node.right)

    return BFS(target, neighbour_dict, K)


test_tree = list2binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
test_t = 5
test_k = 2
print(distanceK(test_tree, test_t, test_k))
