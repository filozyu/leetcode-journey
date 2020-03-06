# Q2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Faster solution (could be better)
def exp_ten(x):
    res = 1
    for i in range(x):
        res *= 10
    return res


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    output = ListNode((l1.val + l2.val) % 10)
    l1_next = l1
    l2_next = l2
    prev_ln = output

    if l1.val + l2.val >= 10:
        pre_addone = 1
    else:
        pre_addone = 0

    while l1_next.next is not None or l2_next.next is not None:
        if l1_next.next is None:
            l1_next_val = 0
            l2_next = l2_next.next
            l2_next_val = l2_next.val

        elif l2_next.next is None:
            l2_next_val = 0
            l1_next = l1_next.next
            l1_next_val = l1_next.val

        else:
            l1_next_val, l2_next_val = l1_next.next.val, l2_next.next.val
            l1_next, l2_next = l1_next.next, l2_next.next

        curr_ln = ListNode((l1_next_val + l2_next_val + pre_addone) % 10)
        prev_ln.next = curr_ln
        prev_ln = curr_ln

        if l1_next_val + l2_next_val + pre_addone >= 10:
            pre_addone = 1
        else:
            pre_addone = 0

    if pre_addone == 1:
        curr_ln = ListNode(1)
        prev_ln.next = curr_ln

    return output
