from utils import list2binary_tree


def isEqual(s_node, t_node):
    """
    Whether the tree whose root is t_node is a subtree in a tree whose root is s_node
    Time: O(m) m - number of nodes in the tree whose root is t_node
    Space: O(m + n) n - number of nodes in the tree whose root is s_node
    """
    s_stack_temp = [s_node]
    t_stack_temp = [t_node]
    while t_stack_temp:
        curr_t = t_stack_temp.pop()
        curr_s = s_stack_temp.pop()
        if curr_s is not None and curr_t is not None and curr_s.val == curr_t.val:
            t_stack_temp.append(curr_t.left)
            t_stack_temp.append(curr_t.right)
            s_stack_temp.append(curr_s.left)
            s_stack_temp.append(curr_s.right)
        elif curr_s is None and curr_t is None:
            continue
        else:
            return False
    return True


def isSubtree(s, t):
    """
    For each node in s, check if it is the same as t, if it is, then check the subtree
    Time: O(mn) in the worst case, invoke isEqual for every node in s
    Space: O(n) n - number of nodes in the tree whose root is s_node
    """
    s_stack = [s]
    while s_stack:
        curr_node = s_stack.pop()
        if curr_node is not None:
            if curr_node.val == t.val and isEqual(curr_node, t):
                return True
            s_stack.append(curr_node.left)
            s_stack.append(curr_node.right)
    return False


test_s_1 = list2binary_tree([3, 4, 5, 1, 2])
test_t_1 = list2binary_tree([4, 1, 2])


test_s_2 = list2binary_tree([3, 4, 5, 1, None, 2])
test_t_2 = list2binary_tree([3, 1, 2])

print(isSubtree(test_s_2, test_t_2))
