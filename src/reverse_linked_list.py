def reverseList_iterative(head):
    """
    Iteration (fast)
    Time: O(n)
    Space: O(1)
    """
    if head is None:
        return None
    head_next = head.next
    prev_head = head
    prev_head.next = None
    while head_next:
        head = head_next
        head_next = head.next
        head.next = prev_head
        prev_head = head
    return head


def reverseList_recursive(head):
    """
    Recursion (slow)
    Time: O(n)
    Space: O(n) - recursion stack
    """
    if head is None or head.next is None:
        return head

    temp_head = head.next
    reverse_head = reverseList_recursive(temp_head)
    temp_head.next = head
    head.next = None
    return reverse_head
