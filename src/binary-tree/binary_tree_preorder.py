from utils import list2binary_tree


def preorderTraversal(root):
    """
    Recursion
    Time: O(n)
    Space: O(H) the recursion stack (H: height of the tree, logn < H < n)

    NOTE: depth first search using stack is equivalent to pre-order
    for any popped node add its right children first then the left children (node.right -> node.left)
    Otherwise we can add right after left, but changing pre-order to go through right branch before left
    """
    res = []
    if root:
        res.append(root.val)
        res += preorderTraversal(root.left)
        res += preorderTraversal(root.right)
    return res


def preorderTraversal_iterative(root):
    """
    Iterative
    Time: O(n)
    Space: O(H) the stack will hold at most H nodes
    """
    res = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node:
            # the oder of appending should be the reverse of the recursive version (stack last in first out)
            # no need to append the val (first step in pre-order) since we can add value directly in result
            # and we no longer need curr_node after popping it out
            # (unlike in-order and post-order where we want the values in later steps)
            res.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
    return res


test = list2binary_tree([1, None, 2, 3])
print(preorderTraversal(test))
print(preorderTraversal_iterative(test))
