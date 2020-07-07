# Easy
def middleNode(head):
    """
    Loop twice
    Time: O(n)
    Space: O(1)
    """
    # first loop to get the length
    length = 1
    curr_node = head.next
    while curr_node:
        curr_node = curr_node.next
        length += 1

    # second loop to get the middle point
    count = 1
    curr_node = head
    while count < length // 2 + 1:
        count += 1
        curr_node = curr_node.next
    return curr_node


def middleNode_two_pointers(head):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    """
    # fast is twice as fast as slow
    slow, fast = head, head
    # at the end of the list, fast could point to the last node (odd length), check fast.next in this case
    # or point to the next of the last node: None (even length), check fast itself in this case
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # when fast is at the end, slow is at the middle
    return slow
