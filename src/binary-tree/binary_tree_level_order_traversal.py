from collections import deque

from utils import list2binary_tree


def levelOrder(root):
    """
    Iterative with queue
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return root
    res = []
    level = 1
    queue = deque([(root, level)])
    while queue:
        curr_node, level = queue.popleft()
        if curr_node.left:
            queue.append((curr_node.left, level + 1))
        if curr_node.right:
            queue.append((curr_node.right, level + 1))
        if len(res) < level:
            res.append([curr_node.val])
        else:
            res[level - 1].append(curr_node.val)

    return res


test = list2binary_tree([3, 9, 20, None, None, 15, 7])
print(levelOrder(test))
