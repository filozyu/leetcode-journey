from collections import deque

from utils import list2binary_tree


def levelOrderBottom(root):
    """
    BFS with deque to store the results (no need to reverse rhe results in the end)
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return root

    res = deque()
    que = deque([(root, 1)])
    while que:
        curr_node, level = que.popleft()
        if curr_node.left:
            que.append((curr_node.left, level + 1))
        if curr_node.right:
            que.append((curr_node.right, level + 1))

        if len(res) < level:
            res.appendleft([curr_node.val])

        else:
            res[0].append(curr_node.val)

    return res


test = list2binary_tree([3, 9, 20, None, None, 15, 7])
print(levelOrderBottom(test))
