from collections import deque

from utils import list2binary_tree


def rightSideView(root):
    """
    BFS, with res storing every node
    Time: O(n)
    Space: O(n) que and res
    """
    if not root:
        return root
    res = []
    que = deque([(root, 1)])
    # similar approach in level order traversal, but only get the last node in every level now (right most node)
    while que:
        curr_node, level = que.popleft()
        if curr_node.left:
            que.append((curr_node.left, level + 1))
        if curr_node.right:
            que.append((curr_node.right, level + 1))

        if len(res) < level:
            res.append([curr_node.val])
        else:
            res[level - 1].append(curr_node.val)

    return [lev[-1] for lev in res]


def rightSideView_alt(root):
    """
    BFS with level indicator
    Time: O(n)
    Space: O(d) d the diameter of the tree, however in worst case D could be n/2 thus O(n)
    """
    if not root:
        return root
    res = []
    # None indicates the end of a level
    que = deque([root, None])
    # maintain curr and prev so that when curr points to None, prev should be the right most node in that layer
    curr = root

    while que:
        prev, curr = curr, que.popleft()
        if curr:
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        else:
            # prev now points to the right most node in the current layer
            res.append(prev.val)
            # just to make sure we won't run into an infinite loop
            if que:
                que.append(None)

    return res


test = list2binary_tree([3, 9, 20, 6, None, 15, 7, 8])
print(rightSideView_alt(test))
