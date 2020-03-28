from utils import list2binary_tree


def maxDepth(root):
    """
    Recursion
    Time: O(n) n: number of nodes in the tree, every node will be visited once
    Space: O(n) (worst case, a line graph) and O(logn) (best case, a balanced tree)
    (space is the size of the recursion stack)
    """
    if not root:
        return 0
    left_tree = root.left
    right_tree = root.right
    return max(maxDepth(left_tree), maxDepth(right_tree)) + 1


def maxDepth_DFS(root):
    """
    Depth first search
    Time: O(n)
    Space: O(n)
    """
    stack = []
    max_depth = 0
    # stack record the current node and the depth of that node
    stack.append((root, 1))
    while stack:
        # note that curr_node can be None ("child" of a leaf) with an hypothetical depth (real depth + 1)
        curr_node, curr_depth = stack.pop()
        if curr_node:
            stack.append((curr_node.left, curr_depth + 1))
            stack.append((curr_node.right, curr_depth + 1))
            # update max_depth only if curr_node an actual node, so this will stop at the leaves
            if curr_depth > max_depth:
                max_depth = curr_depth
    return max_depth


def maxDepth_BFS(root):
    """
    Breadth first search
    Time: O(n)
    Space: O(n)
    """
    # similar to DFS, just replace the stack with a queue
    from collections import deque
    que = deque()
    max_depth = 0
    que.append((root, 1))
    while que:
        curr_node, curr_depth = que.popleft()
        if curr_node:
            que.append((curr_node.left, curr_depth+1))
            que.append((curr_node.right, curr_depth+1))
            if curr_depth > max_depth:
                max_depth = curr_depth
    return max_depth


test_tree = list2binary_tree([1, 2, 3, None, None, 4, 5, 6, 7, 8])
print(maxDepth_BFS(test_tree))
