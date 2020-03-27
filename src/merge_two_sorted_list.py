from utils import ListNode2list, list2ListNode, ListNode


def mergeTwoLists(l1, l2):
    """
    Straight forward merge
    Time: O(m+n), m = len(l1), n = len(l2)
    Space: O(1)
    """
    # Assignment such as a = l1 (l1 is a ListNode)
    # will assign the address to start, change of a's `next` or `val` will result in change in l1's `next` or `val`
    # because the changes were made to the object stored in the common address
    # similarly if two assignments were made of the same variable: a, b =l1, l1
    # then change of a's `next` or `val` will result in change in b's and l1's
    # If reassign a to another ListNode say l2, a = l2, then change of a will not affect that of b and l1

    # Summary: Changing an object's properties through one of its assigned variable will change the object itself and
    # all the other assigned variables

    curr = ListNode(-1)  # auxiliary head pointer to retrieve the whole list
    start = curr
    while l1 is not None or l2 is not None:
        # if one of them is empty and then append the other to the end of the result and return
        if l1 is None:
            curr.next = l2
            return start.next
        elif l2 is None:
            curr.next = l1
            return start.next
        # if both are non-empty
        if l1.val < l2.val:
            # below will append all nodes of l1 to curr, `start` will change at the same time
            # e.g. curr = [3, 5], l1 = [4, 6], l2 = [5], start = [-1, 1, 2, 3, 5]
            # then after the execution, curr = [3, 4, 6], start = [-1, 1, 2, 3, 4, 6]
            curr.next = l1
            # below will advance l1 by 1 node
            # following the above example, after execution, l1 = [6]
            l1 = l1.next
            # below will advance curr by 1 node, and has no effect on `start`
            # since curr will be assigned to a new ListNode (curr.next)
            # and no changes were made to existing nodes
            # following the above example, after execution, curr = [4, 6], l1 = [6], l2 = [5]
            # in the next iteration, enter l2.val < l1.val and curr will be [4, 5]...
            curr = curr.next
        else:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

    return start.next


def mergeTwoLists_recur(l1, l2):
    """
    Recursion
    Time: O(m+n), m = len(l1), n = len(l2)
    Space: O(m+n), size of the recursion stack
    """
    # res =
    # 1) l1[0] + merge(l1[1:], l2) if (l1[0] < l2[0])
    # 2) l2[0] + merge(l1, l2[1:]) if (l1[0] >= l2[0])
    # if l1 or l2 empty, append the non-empty list
    # recursion ends if either one of the two is empty
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists_recur(l1.next, l2)
        # return the merged list
        return l1
    else:
        l2.next = mergeTwoLists_recur(l1, l2.next)
        # return the merged list
        return l2


test1, test2 = list2ListNode([1, 3, 5]), list2ListNode([2, 4, 6])
print(test1, test2)
print(ListNode2list(mergeTwoLists_recur(test1, test2)))
