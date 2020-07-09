from utils import list2ListNode, ListNode2list, ListNode


def removeElements(head, val):
    """
    Linear search with pseudo head
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head
    prev_node = return_head = ListNode(-1)
    return_head.next = head
    while head:
        if head.val == val:
            prev_node.next = head.next
            head = head.next
        else:
            prev_node = head
            head = head.next
    return return_head.next


test = list2ListNode([1, 2, 6, 3, 4, 5, 6])
print(
    ListNode2list(
        removeElements(test, 6)
    )
)
