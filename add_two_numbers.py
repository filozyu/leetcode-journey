# Q2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
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

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1_list = []
    l2_list = []
    l1_num = l1
    l2_num = l2
    l1_val = 0
    l2_val = 0
    while l1_num is not None:
        l1_list.append(l1_num.val)
        l1_num = l1_num.next
    for i in range(len(l1_list)):
        l1_val += l1_list[i]*exp_ten(i)

    while l2_num is not None:
        l2_list.append(l2_num.val)
        l2_num = l2_num.next
    for i in range(len(l2_list)):
        l2_val += l2_list[i]*exp_ten(i)

    res_sum = l1_val + l2_val
    first_node = ListNode(int(res_sum%10))
    prev_node = first_node
    res_sum = (res_sum - (res_sum % 10))/10
    while res_sum != 0:
        curr_node = ListNode(int(res_sum%10))
        prev_node.next = curr_node
        res_sum = (res_sum - (res_sum % 10))/10
        prev_node = curr_node

    return first_node
