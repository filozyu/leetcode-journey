from utils import list2ListNode, ListNode2list, ListNode


def deleteDuplicates(head):
    """
    Delete neighbouring nodes with the same value
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head
    return_head = ListNode(-1)
    return_head.next = head

    # loop invariant:
    # All nodes in the list up to the pointer head do not contain duplicate elements.
    while head.next:
        if head.next.val == head.val:
            head.next = head.next.next
        else:
            head = head.next
    return return_head.next


test = list2ListNode([1, 1, 2, 3])
print(
    ListNode2list(
        deleteDuplicates(test)
    )
)
