from merge_two_sorted_list import mergeTwoLists
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
    mid = int(len(lists)/2)
    # Recursion tree time and space complexity:
    # TIME: The tree breadth (how many total recursive function calls will be made)
    # SPACE: The tree depth (how many total return statements will be executed until the base case)
    return mergeTwoLists(
        mergeKLists_two_recursion(lists[:mid]),
        mergeKLists_two_recursion(lists[mid:])
    )


def mergeKLists_priority_queue(lists):
    return None


test_list = [[1,4,5],[1,3,4],[2,6]]
# test_list = [[],[]]
test = [list2ListNode(in_ln) for in_ln in test_list]
print(ListNode2list(mergeKLists_two_recursion(test)))
