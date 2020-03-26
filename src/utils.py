from time import perf_counter


# Data Structure
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Methods
def timer(num_trails, call_func, *args, **kwargs):
    start = perf_counter()
    for i in range(num_trails):
        call_func(*args, **kwargs)
    end = perf_counter()
    thresh_avg_time = float(end - start) / num_trails
    return thresh_avg_time


def list2ListNode(input_list):
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