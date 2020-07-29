from utils import list2binary_tree


def rob(root):
    """
    Dynamic programming on trees (post order traversal)
    Time: O(n) n - number of nodes in the tree
    Space: O(logn) the depth of the tree (recursion stack)
    """

    def dfs(node):
        # dfs returns a list of two numbers:
        # dp[0] denotes the max profit of the subtree rooting at node WITHOUT robbing node
        # dp[1] denotes the max profit of the subtree rooting at node WITH robbing node
        if node is None:
            return [0, 0]

        left = dfs(node.left)
        right = dfs(node.right)

        dp = [0, 0]

        # if node has not been robbed, then its children can be either robbed or not
        dp[0] = max(left[0], left[1]) + max(right[0], right[1])
        # if node has been robbed, then its children must not be robbed
        dp[1] = node.val + left[0] + right[0]

        return dp

    # res[0] is the max profit if root has been robbed
    # res[1] is the max profit if root has not been robbed
    res = dfs(root)

    return max(res)


test = list2binary_tree([3, 2, 3, None, 3, None, 1])
print(rob(test))
