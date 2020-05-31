# Return a deepcopy of the linked list


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    """
    Iterative with a visited-copy dictionary
    Time: O(n), two passes, one for copying the spine of the list, one for adding random links
    Space: O(n), the dictionary
    """
    if not head:
        return None
    prev_node = head
    copy_head = Node(head.val)
    copy_prev = copy_head
    copy_dict = {head: copy_head}

    while prev_node.next is not None:
        next_node = prev_node.next
        copy_prev.next = Node(next_node.val)
        prev_node = next_node
        copy_prev = copy_prev.next
        copy_dict[prev_node] = copy_prev

    prev_node = head
    while prev_node is not None:
        rand_node = prev_node.random
        if rand_node is None:
            copy_dict[prev_node].random = None
        copy_dict[prev_node].random = copy_dict[rand_node]
        prev_node = prev_node.next

    return copy_head


def copyRandomList_one_pass(head):
    """
    Iterative with a visited-copy dictionary
    Time: O(n), one passes, copying the spine of the list and adding random links
    Space: O(n), the dictionary
    """
    def check_copy_dict(copy_dict, node):
        if node is None:
            return None
        if copy_dict.get(node):
            return copy_dict[node]
        else:
            copy_dict[node] = Node(node.val)
            return copy_dict[node]

    if not head:
        return None
    prev_node = head
    copy_dict = {}

    while prev_node is not None:
        copy_prev = check_copy_dict(copy_dict, prev_node)
        next_node = prev_node.next
        copy_next = check_copy_dict(copy_dict, next_node)
        rand_node = prev_node.random
        copy_rand = check_copy_dict(copy_dict, rand_node)
        copy_prev.next = copy_next
        copy_prev.random = copy_rand
        prev_node = next_node

    return copy_dict[head]
