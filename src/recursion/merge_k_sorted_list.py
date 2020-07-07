from dataclasses import dataclass, field
from typing import Any

from recursion.merge_two_sorted_list import mergeTwoLists
from utils import list2ListNode, ListNode2list, ListNode


def mergeKLists(lists):
    """
    Straight forward merge sort
    Time: O(kn), k: number of lists (len(lists)); n: number of nodes in total
    Space: O(1) (?) does lists take space?
    """
    # head to return
    head = ListNode(-1)
    prev_node = head
    # remove empty lists
    lists = [i for i in lists if i]
    # while loop: O(n)
    while lists:
        curr_min = lists[0].val
        min_ind = 0
        # find min in the heads: O(k)
        for i in range(len(lists)):
            if lists[i].val < curr_min:
                curr_min = lists[i].val
                min_ind = i
        # link the min to result and update the advance the list where the min was by one
        # remove the list from lists if the last node is the min
        prev_node.next = lists[min_ind]
        prev_node = lists[min_ind]
        lists[min_ind] = lists[min_ind].next
        if lists[min_ind] is None:
            lists.pop(min_ind)

    return head.next


def mergeKLists_two_recursion(lists):
    """
    Recursive merge sort (divide and conquer)
    Time: O(nlogk) n: merge two lists at every layer; logk: number of layers
    Space: O(logk) depth of the recursion tree
    """
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 0:
        return None
    mid = int(len(lists) / 2)
    # Recursion tree time and space complexity:
    # TIME: The tree breadth (how many total recursive function calls will be made)
    # SPACE: The tree depth (how many total return statements will be executed until the base case)
    return mergeTwoLists(
        mergeKLists_two_recursion(lists[:mid]), mergeKLists_two_recursion(lists[mid:])
    )


@dataclass(order=True)
class PrioritizedItem:
    """
    Require Python 3.7 (running on 3.7.7)
    Wrapper for listnodes, in case two ln have the same priority number
    this will prevent the priority queue to compare the ln
    """

    priority: int
    item: Any = field(compare=False)


class Wrapper:
    """
    Alternative wrapper for listnodes
    """

    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


def mergeKLists_priority_queue(lists):
    """
    Priority queue
    Time: O(nlogk) logk: insertion and removal time of priority queue
    Space: O(k) the size of the priority queue, assuming the returned node list only take one extra node (head)
    """
    from queue import PriorityQueue

    # Priority queue is a queue with priority, and instead of first in first out,
    # the element with highest priority (minimum priority number) will be retrieved first
    # doing this allows us retrieve the node with the smallest value with O(logk),
    # but insertion can also take O(logk)
    # without priority queue, we can use the method in the first solution, find min node in a loop O(k)
    head = ListNode(-1)
    prev_node = head
    q = PriorityQueue()
    for ln in lists:
        if ln:
            # wrapper here and below to prevent priority queue from comparing listnodes with the same priority
            q.put(PrioritizedItem(ln.val, ln))
            # OR use q.put(Wrapper(ln))

    while not q.empty():
        node = q.get().item
        # OR use node = q.get().node
        prev_node.next = node
        prev_node = node
        if node.next:
            q.put(PrioritizedItem(node.next.val, node.next))
            # OR use q.put(Wrapper(node.next))
    return head.next


test_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
# test_list = [[],[]]
test = [list2ListNode(in_ln) for in_ln in test_list]
print(ListNode2list(mergeKLists_priority_queue(test)))
