from utils import list2ListNode, ListNode2list, ListNode


def deleteDuplicates(head):
    """
    Remove all duplicates but the first and finally itself
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    # setup the pseudo head
    return_head = ListNode(-1)
    return_head.next = head
    # prev_node is last the non-duplicate node
    prev_node = return_head

    while head.next:
        # store the value, to delete the first occurrence of the duplicates
        curr_val = head.val
        # remove the duplicates (from second occurrences onwards) by cutting the links
        if head.val == head.next.val:
            head.next = head.next.next

            # the following lines are used to remove the first occurrence of the duplicate
            # 1. the duplicates are towards the end, then link the last non-duplicate node to None
            if not head.next:
                prev_node.next = None
            # 2. the duplicates are in the middle, move pass head (which is the first occurrence)
            # by linking the next node (different val from head) to prev_node as a potential candidate
            elif head.next.val != curr_val:
                prev_node.next = head.next
                head = head.next

        # we entered the else statement if head is a non-duplicate node, update prev_node to be it and move ahead
        else:
            prev_node = head
            head = head.next

    return return_head.next


def deleteDuplicates_last(head):
    """
    Remove all duplicates but the last and finally itself
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    # setup the pseudo head
    return_head = ListNode(-1)
    return_head.next = head
    # prev_node is last the non-duplicate node
    prev_node = return_head

    # head could be None here
    while head and head.next:

        if head.val == head.next.val:
            # keep on moving forward until head is now the last occurrence
            while head.next and head.val == head.next.val:
                head = head.next
            # skip the last occurrence, NOTE: the new head could be None
            head = head.next
            prev_node.next = head

        else:
            prev_node = head
            head = head.next

    return return_head.next


test = list2ListNode([1, 2, 3, 3, 4, 4, 5, 6, 6])
print(ListNode2list(deleteDuplicates(test)))
