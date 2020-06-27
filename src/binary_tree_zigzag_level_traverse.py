# BFS, DFS, Double ended queue
from collections import deque

from utils import list2binary_tree


def zigzagLevelOrder(root):
    """
    Queue with odd and even layers
    Time: O(N) N is the number of nodes in the tree
    Space: O(N) the queue, note that if the tree is complete, the final layer contains (N + 1) / 2 - 1 nodes
    """
    q = deque()
    if not root:
        return []
    q.append(root)
    q.append("|")
    # temp here is for the storage of a layer's values
    temp = []
    # res is for the final answer
    res = []
    # num_layer's parity will determine from which way should a layer's nodes be traversed
    num_layer = 0
    while q:
        curr_node = q.popleft()
        # when curr_node is an actual node
        if curr_node is not None and curr_node != "|":
            # check the children before appending,
            # if append without checking, we will append all the None "children" of the last layer,
            # and the queue will contain 2^(L+1) nodes after scanning through the last layer,
            # which is N + 1 None!
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            temp.append(curr_node.val)
        # when curr_node is "|"
        # NOTE: temp will be empty after we've finished with the last layer,
        # but the while loop will break before we append the empty list
        elif curr_node == "|":
            num_layer += 1
            # to maintain the zigzag pattern
            if num_layer % 2 == 0:
                # suppose there are K nodes, the reversion will be O(K)
                res.append(temp[::-1])
            else:
                res.append(temp)
            # don't forget to erase temp for the next layer
            temp = []
            if q:
                q.append("|")
        # when curr_node is None
        else:
            continue
    return res


def zigzagLevelOrder_deque(root):
    """
    Queue with odd and even layers, same as above but temp is also a deque
    Time: O(N) N is the number of nodes in the tree
    Space: O(N) the queue, note that if the tree is complete, the final layer contains (N + 1) / 2 - 1 nodes
    """
    q = deque()
    if not root:
        return []
    q.append(root)
    q.append("|")
    # temp here is for the storage of a layer's values
    temp = deque()
    # res is for the final answer
    res = []
    # num_layer's parity will determine from which way should a layer's nodes be traversed
    num_layer = 1
    while q:
        curr_node = q.popleft()
        # when curr_node is an actual node
        if curr_node is not None and curr_node != "|":
            # check the children before appending,
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            # depending on the layer, append the node to head or to tail
            # note that it will cost O(n) to append to head in a list
            # O(1) in a deque
            if num_layer % 2 == 0:
                temp.appendleft(curr_node.val)
            else:
                temp.append(curr_node.val)
        # when curr_node is "|"
        elif curr_node == "|":
            num_layer += 1
            # here the res contains deque object, not list
            # if list is forced to be the returned type, we have to convert which will again be O(n)
            # but here we can get away without converting deque to list
            res.append(temp)
            # don't forget to erase temp for the next layer
            temp = deque()
            if q:
                q.append("|")
        # when curr_node is None
        else:
            continue
    return res


def zigzagLevelOrder_dfs(root):
    """
    Stack with odd and even layers, use deque to store the values in each layer
    Time: O(N) N is the number of nodes in the tree
    Space: O(logN) the stack will only store nodes that is at most the height of the tree
    """
    stack = []
    if not root:
        return []
    # Append (node, level) to the stack
    stack.append((root, 1))
    # res is for the final answer
    res = []
    while stack:
        curr_node, level = stack.pop()

        if curr_node.left:
            stack.append((curr_node.left, level + 1))
        if curr_node.right:
            stack.append((curr_node.right, level + 1))

        # if visiting a node from a new level for the first time
        if len(res) < level:
            res.append(deque([curr_node.val]))
        # else the deque for the level already exists, append (left or right) to it
        else:
            if level % 2 == 0:
                res[level - 1].append(curr_node.val)
            else:
                res[level - 1].appendleft(curr_node.val)

    return res


test = list2binary_tree([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, 10, None, None])
print(zigzagLevelOrder_dfs(test))
