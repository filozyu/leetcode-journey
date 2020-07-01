from utils import list2binary_tree


def diameterOfBinaryTree(root):
    def get_children_length(node, curr_max):
        if not node:
            return -1, curr_max
        left_len, curr_max = get_children_length(node.left, curr_max)
        right_len, curr_max = get_children_length(node.right, curr_max)
        curr_max = max(curr_max, left_len + right_len + 2)

        return max(left_len + 1, right_len + 1), curr_max

    _, max_len = get_children_length(root, 0)

    return max_len


test = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]

# test = [1,2,3,4,5]
test_tree = list2binary_tree(test)
print(diameterOfBinaryTree(test_tree))
