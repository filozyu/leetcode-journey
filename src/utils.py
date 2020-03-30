from collections import deque
from time import perf_counter

# Data Structure #


# linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Methods #
def timer(num_trails, call_func, *args, **kwargs):
    start = perf_counter()
    for i in range(num_trails):
        call_func(*args, **kwargs)
    end = perf_counter()
    thresh_avg_time = float(end - start) / num_trails
    return thresh_avg_time


def list2ListNode(input_list):
    if not input_list:
        return None
    head = ListNode(input_list[0])
    curr = head
    if len(input_list) >= 2:
        for i in input_list[1:]:
            curr.next = ListNode(i)
            curr = curr.next
    return head


def ListNode2list(input_listnode):
    res = []
    curr = input_listnode
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def list2binary_tree(input_list):
    """
    Build binary tree from the given input list
    :param input_list: start with root, None should be inserted to indicate leaf nodes (the last layer can be inferred)
    :return: root, TreeNode
    """
    # e.g. [1, 2, 3, None, None, 4, 5, 6, 7, 8]
    #     1
    #   /  \
    #  2    3
    #     /   \
    #    4    5
    #   /\   /
    #  6 7  8
    visited = deque()
    root = TreeNode(input_list[0])
    input_list.pop(0)
    visited.append(root)
    while len(input_list) > 0:
        curr_node = visited.popleft()
        if not curr_node:
            continue
        if input_list[0]:
            left_child = TreeNode(input_list.pop(0))
        else:
            left_child = input_list.pop(0)
        if len(input_list) == 0:
            curr_node.left = left_child
            break
        if input_list[0]:
            right_child = TreeNode(input_list.pop(0))
        else:
            right_child = input_list.pop(0)
        curr_node.left = left_child
        curr_node.right = right_child
        visited.append(left_child)
        visited.append(right_child)

    return root
