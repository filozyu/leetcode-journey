from utils import list2binary_tree, TreeNode


def postorderTraversal(root):
    """
    Recursion
    Time: O(n)
    Space: O(H) the recursion stack (H: height of the tree, logn < H < n)
    """
    res = []
    if root:
        res += postorderTraversal(root.left)
        res += postorderTraversal(root.right)
        res.append(root.val)
    return res


def postorderTraversal_iterative(root):
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
            # we stores value separately since we will visit the root value last
            # but we don't want to process the root as a node again (already been processed to get left/right)
            if isinstance(curr_node, TreeNode):
                # fist append the value (which will be popped out last)
                # then append the right child (which will be popped out penultimately)
                # finally append the left child (which will be popped out first)
                stack.append(curr_node.val)
                if curr_node.right:
                    stack.append(curr_node.right)
                if curr_node.left:
                    stack.append(curr_node.left)
            else:
                # if the popped element is not a TreeNode, it must be the values of roots
                res.append(curr_node)
    return res


def postorderTraversal_iterative_alt(root):
    """
    Iterative, but the stack only contains TreeNode
    KEY:
    1) push in stack: node.right -> node -> node.left
    2) when popping, swap the popped node if its right child is on the top of the stack

    Time: O(n)
    Space: O(H)
    """
    res = []
    stack = []
    curr_node = root
    while stack or curr_node:
        # the order of nodes that are pushed to the stack: node.right -> node -> node.left
        # since the visiting order is:
        # node.left (all nodes under) -> node.right (all nodes under) -> node
        # the reason that we are in favour of this ordering as opposed to node -> node.right -> node.left
        # is that we are not sure whether the left branch or the right branch of node has been visited
        # when we pop out node.
        # But by using node.right -> node -> node.left we know that the right child of node (if any)
        # is always on the top of the stack when we popped node out

        # To make sure we have visited the node.right before visiting node,
        # we will swap the node with its right child upon popped out of the stack,
        # that is node is now at the top of the stack and the node.right is the one we are processing

        # In post-order traversal, the leftmost leaf node is always visited first,
        # then the right branch (say RB) of that node's parent is visited,
        # also the leftmost leaf node in that branch (RB) will be visited first

        # If A's parent does have a right child and that child is a leaf node, then visit it
        # If A is the only child of its parent (no right branch), then its parent is visited

        # A node will always be popped before its right child,
        # so we need to swap node and its right child when processing

        # when a node is popped, check if it is the leftmost leaf node in the REMAINING NODES
        # if it is the leftmost leaf node: only check whether it has a right child,
        # note that here we don't need to check for left child since we must have visited it if there is any,

        # otherwise swap it with the last node in stack (its right child)
        # do not append anything to the result, but enter the next iteration (visit the right branch)
        while curr_node:
            if curr_node.right:
                stack.append(curr_node.right)
            stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = stack.pop()

        # if we have not yet visited the right branch of curr_node (i.e. curr_node is not a leaf in the remaining nodes)
        if stack and curr_node.right == stack[-1]:
            # put curr_node on the top of the stack
            # and start to process the right branch of curr_node in the next iteration
            stack[-1] = curr_node
            curr_node = curr_node.right

        # otherwise we have processed left (before the node) and right (after the swapping, if any) branch of curr_node
        # (i.e. curr_node is a leaf in the remaining nodes)
        else:
            res.append(curr_node.val)
            curr_node = None

    return res


test = list2binary_tree([1, 2, 3, 4, 5])
print(postorderTraversal(test))
print(postorderTraversal_iterative(test))
