from utils import list2ListNode, ListNode2list


def rotateRight(head, k):
    """
    Iteratively find new tail
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    # the following block will get the length of the list and the last node in the list (last)
    curr = head
    length = 1
    while curr.next:
        curr = curr.next
        length += 1
    last = curr

    # k is transformed to be between 0 and length - 1
    k = k % length

    # loop through the list to find the new tail, which is the n-k th node from the start
    curr = head
    for _ in range(1, length - k):
        curr = curr.next

    # if the new tail is also the old tail (last), which will happen if k == 0
    # then the list does not change after rotation
    if not curr.next:
        return head

    # if new tail is different from old tail, set new tail as the tail and link old tail to the original head
    tail = curr
    new_head = curr.next
    # remember to remove the rest from the new tail
    tail.next = None
    last.next = head
    return new_head


test = list2ListNode([1])
test_k = 3
print(ListNode2list(rotateRight(test, test_k)))
