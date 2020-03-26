from utils import ListNode2list, list2ListNode


def removeNthFromEnd(head, n):
    """
    One pass dictionary
    Time: O(L), L here the length of the list
    Space: O(L)
    """
    # Remove nothing
    if n == 0:
        return head
    curr = head
    record = {}
    i = 0
    while curr:
        record[i] = curr
        curr = curr.next
        i += 1

    # find the index of the node to be removed
    rm_ind = len(record) - n
    # if the first node is to be removed and there are more nodes
    if rm_ind == 0 and len(record) > 1:
        return record[1]
    # if the first node is to be removed and there are no more nodes
    elif rm_ind == 0:
        return None
    # if the last node is to be removed
    if n == 1:
        record[rm_ind - 1].next = None
    # normal cases
    else:
        record[rm_ind - 1].next = record[rm_ind + 1]
    return head


def removeNthFromEnd_two_pointers(head, n):
    """
    Two pointers
    Time: O(L)
    Space: O(1)
    """
    # Remove nothing
    if n == 0:
        return head
    # if the list only has one node and n > 0, then remove the only node
    elif head.next is None:
        return None
    # initialise the two pointers
    left = head
    right = head
    i = 0
    while right.next is not None:
        right = right.next
        # the second pointer (left) is n steps behind the first pointer (right)
        if i == n:
            left = left.next
        # keep advance right pointer until the gap from the first node is n
        elif i < n:
            i += 1
    # if the last node is to be removed
    if n == 1:
        left.next = None
    # if the i did not reach n before right pointer hit the last node
    # then n is greater or equal to the length (L) of the list
    # and since n is a valid number, it must be L
    # remove the first node
    elif i < n:
        return head.next
    # normal cases, note here left.next is the node we want to remove
    else:
        left.next = left.next.next
    return head


# test = [1,2,3,4,5]
# n= 2

# test = [1,2]
# n = 2

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 7
test_ln = list2ListNode(test)

print(test)
print(ListNode2list(removeNthFromEnd_two_pointers(test_ln, n)))
