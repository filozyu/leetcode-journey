from utils import list2ListNode, ListNode2list, ListNode


def reverseBetween(head, m, n):
    """
    Iterative reversing with multiple pointers
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    count = 1
    return_head = ListNode(-1)
    return_head.next = head
    # start points to the node before the reversed part (i.e. m-1 th node in the list)
    start = return_head
    # prev points to the head of the reversed part
    # last points to the end of the reversed part
    prev = last = head
    # curr points to the node we are currently looking at
    curr = head.next

    while curr:

        # if we have not reached the part that needs to be reversed
        if count < m:
            # start is one step before last while count < m, but will fix once count >= m
            # before getting into the need-to-reverse part, last and start point to the same node
            # curr is one step ahead of last
            last = last.next
            start = start.next
            prev = prev.next
            curr = curr.next
        # the elif statement will run only if n > m
        elif m <= count <= n - 1:
            # get next_node, this will be curr in the next step
            next_node = curr.next
            # connect the next to the end of the reversed part
            last.next = next_node
            # prev always points to the head of the reversed part
            # append the reversed part to curr
            curr.next = prev
            # curr is now the new head of the reversed part
            start.next = curr

            # update prev and curr to be consistent with their definitions
            prev = curr
            curr = next_node

        # else we are outside the part that needs to be reversed
        else:
            break

        count += 1

    return return_head.next


test = list2ListNode([1, 2, 3, 4, 5])
print(ListNode2list(reverseBetween(test, 1, 5)))
