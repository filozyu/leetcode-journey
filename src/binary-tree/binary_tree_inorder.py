from utils import list2binary_tree, TreeNode


def inorderTraversal(root):
    """
    Recursion
    Time: O(n)
    Space: O(H) the recursion stack (H: height of the tree, logn < H < n)
    """
    res = []
    if root:
        res += inorderTraversal(root.left)
        res.append(root.val)
        res += inorderTraversal(root.right)
    return res


def inorderTraversal_iterative(root):
    """
    Iterative
    Time: O(n)
    Space: O(H) the stack will hold at most H nodes/values
    """
    res = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node:
            # stack contains two types of data:
            # 1) TreeNode
            # 2) value of a TreeNode (could be int, float, etc.)
            # we stores value separately since we will visit the root value in the middle
            # but we don't want to process the root as a node again (already been processed to get left/right)
            if isinstance(curr_node, TreeNode):
                # fist append the right child (which will be popped out last)
                # then append the node value (which will be popped out penultimately)
                # finally append the left child (which will be popped out first)
                if curr_node.right:
                    stack.append(curr_node.right)
                stack.append(curr_node.val)
                if curr_node.left:
                    stack.append(curr_node.left)
            else:
                # if the popped element is not a TreeNode, it must be the values of roots
                res.append(curr_node)
    return res


def inorderTraversal_iterative_alt(root):
    """
    Iterative, but the stack only contains TreeNode
    Time: O(n)
    Space: O(H)
    """
    res = []
    stack = []
    curr_node = root
    while stack or curr_node:
        # push all the left nodes to the current node in (right children not included)
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        # then popped node must be the left most node in the unvisited nodes
        curr_node = stack.pop()
        # at this point all curr_node's left branch has been visited, visit curr_node
        res.append(curr_node.val)
        # next move to the right branch of curr_node and start to visit its left branch (in the next iteration)
        curr_node = curr_node.right

    return res


test = list2binary_tree([1, None, 2, 3])
print(inorderTraversal(test))
print(inorderTraversal_iterative(test))
