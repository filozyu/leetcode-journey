from utils import ListNode2list, list2ListNode, ListNode


def swapPairs(head):
    """
    Recursion
    Time: O(n), depth of recursion
    Space: O(n), recursion stack
    """
    if head is None or head.next is None:
        # if head is None: even, all pairs have been swapped, return None
        # if head.next is None: odd, only one node left, append it
        # NOTE: head is None should be placed in front of OR
        # since if that is evaluated as False, there is no need to check the second statement
        # which could throw an exception since None does not have next
        return head
    else:
        # preserve the head
        temp_head = head
        # preserve the node after the pair
        temp_next = head.next.next
        # swap head and head.next
        head = head.next
        head.next = temp_head
        # append the rest to the swapped pairs
        temp_head.next = swapPairs(temp_next)
        return head


def swapPairs_loop(head):
    """
    Loop
    Time: O(n) (but in runtime slower than recursion)
    Space: O(1) (but in runtime similar to recursion)
    """
    # dummy head for return
    start = ListNode(-1)
    start.next = head
    # var to contain the previous node
    prev_node = start
    # stop the loop if only one or zero node left
    while head and head.next:
        # the current two nodes to be swapped
        first_node = head
        second_node = head.next

        # swap, and linked the second node in the pair to the previous node
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # update previous node to the next pair
        # update head to the first node in the next pair
        prev_node = first_node
        head = first_node.next

    return start.next


test = list2ListNode([1, 2, 3, 4, 5])
# print(ListNode2list(swapPairs(test)))
print(ListNode2list(swapPairs_loop(test)))
