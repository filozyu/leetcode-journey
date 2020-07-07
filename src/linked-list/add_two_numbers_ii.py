# stack
from utils import ListNode, list2ListNode, ListNode2list


def reverse_linked_list(head):
    if not head:
        return head
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


def addTwoNumbers(l1, l2):
    """
    Reverse the lists and then sum
    Time: O(m+n), m the length of l1 and n the length of l2
    Space: O(m+n) since we have reversed the lists
    """
    addone = 0
    head = ListNode(-1)
    curr_node = head

    l1 = reverse_linked_list(l1)
    l2 = reverse_linked_list(l2)

    while l1 is not None or l2 is not None:
        if not l1:
            l1 = ListNode(0)
        elif not l2:
            l2 = ListNode(0)

        curr_sum = l1.val + l2.val + addone
        l1, l2 = l1.next, l2.next
        curr_node.next = ListNode(curr_sum % 10)
        curr_node = curr_node.next
        if curr_sum >= 10:
            addone = 1
        else:
            addone = 0

    if addone == 1:
        curr_node.next = ListNode(1)

    return reverse_linked_list(head.next)


def addTwoNumbers_stack(l1, l2):
    """
    Stack (without reversing the lists)
    Time: O(m+n)
    Space: O(m+n) the two stacks
    """
    addone = 0
    head = None
    l1_stack, l2_stack = [], []
    while l1:
        l1_stack.append(l1.val)
        l1 = l1.next
    while l2:
        l2_stack.append(l2.val)
        l2 = l2.next

    while l1_stack or l2_stack:
        if len(l1_stack) == 0:
            l1_val, l2_val = 0, l2_stack.pop()
        elif len(l2_stack) == 0:
            l1_val, l2_val = l1_stack.pop(), 0
        else:
            l1_val, l2_val = l1_stack.pop(), l2_stack.pop()

        curr_sum = l1_val + l2_val + addone
        curr_node = ListNode(curr_sum % 10)
        curr_node.next = head
        head = curr_node

        if curr_sum >= 10:
            addone = 1
        else:
            addone = 0

    if addone == 1:
        new_head = ListNode(1)
        new_head.next = head
        return new_head
    else:
        return head


test_1 = list2ListNode([2])
test_2 = list2ListNode([8])
print(ListNode2list(addTwoNumbers(test_1, test_2)))
