from utils import list2ListNode, ListNode2list, ListNode


def reverse(head):
    if not head:
        return head
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def reorderList_reverse(head):
    """
    Iteratively link to reversed list
    Time: O(n^2) n iterations, in each iteration the reversion will be O(n)
    Space: O(1)
    """
    if head:
        curr = head

        while curr:
            next_node = curr.next
            curr.next = reverse(next_node)
            curr = curr.next


def reorderList(head):
    """
    Reverse the second half of the list and merge with the first half
    Time: O(n)
    Space: O(1)
    """
    if head:
        # use fast and slow pointers to get to the middle of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # if slow.next is None, it means the list has at most 2 nodes, no need to reorder
        if slow.next:

            # get the right and the left lists that we wish to merge
            right_head = slow.next
            right = reverse(right_head)
            left = head
            # cut the link of the first half to the second half
            slow.next = None

            # pseudo head to store the merged list, head will be the next node to return_head
            return_head = ListNode(-1)
            curr = return_head
            # merge the two lists, in every iteration, first link the left to the merged list then the right
            while left and right:
                left_next = left.next
                right_next = right.next
                # link first the left then the right
                curr.next = left
                curr.next.next = right
                # update the end of the merged list
                curr = right
                # move forward left and right
                left = left_next
                right = right_next
            # if right is still not empty
            if right:
                curr.next = right
            # else left is still not empty
            else:
                curr.next = left


test = list2ListNode([1, 2, 3, 4, 5])
reorderList(test)
print(ListNode2list(test))
