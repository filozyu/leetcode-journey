# merge sort
from utils import list2ListNode, ListNode2list, ListNode


def sortList(head):
    length = 0
    sorted_head = head
    curr_node = head
    while curr_node:
        length += 1
        curr_node = curr_node.next

    left_half, right_half = split_list(head, length // 2)
    if left_half and right_half:
        left_half = sortList(left_half)
        right_half = sortList(right_half)
        sorted_head = merge_sorted_list(left_half, right_half)

    return sorted_head


def split_list(head, length):
    if head and length > 0:
        left = head
        prev = head
        while length > 0 and head:
            length -= 1
            prev = head
            head = head.next
        prev.next = None
        right = head
        return left, right
    else:
        return None, None


def merge_sorted_list(head1, head2):
    sort_head = ListNode(-1)
    prev_node = sort_head
    while head1 or head2:
        if head2 is None:
            prev_node.next = head1
            break
        elif head1 is None:
            prev_node.next = head2
            break
        else:
            if head1.val < head2.val:
                prev_node.next = head1
                prev_node = head1
                head1 = head1.next
            else:
                prev_node.next = head2
                prev_node = head2
                head2 = head2.next
    return sort_head.next


def sortList_top_down(head):
    """
    Merge sort, recursion
    Time: O(nlogn)
    Space: O(logn) recursion stack
    """
    if not head or not head.next:
        return head
    # use two pointers to find the middle point
    # fast pointer moves twice as fast as the slow one
    slow, fast = head, head.next
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # sort recursively
    mid = slow.next
    # slow was connected all the way to the end, break the link to stop in the middle
    slow.next = None
    sorted_left = sortList_top_down(head)
    sorted_right = sortList_top_down(mid)

    # merge the two sorted list
    return_head = ListNode(-1)
    curr_node = return_head
    while sorted_left and sorted_right:
        if sorted_right.val > sorted_left.val:
            curr_node.next = sorted_left
            sorted_left = sorted_left.next
        else:
            curr_node.next = sorted_right
            sorted_right = sorted_right.next
        curr_node = curr_node.next

    if sorted_left:
        curr_node.next = sorted_left
    else:
        curr_node.next = sorted_right

    return return_head.next


def sortList_bottom_up(head):
    """
    Merge list from bottom up
    Time: O(nlogn)
    Space: O(1)
    """
    subarray_len = 1
    length = 0
    curr_node = head
    # get the length of the list
    while curr_node:
        length += 1
        curr_node = curr_node.next

    return_head = ListNode(-1)
    return_head.next = head
    # keep on merging until the whole array is one subarray
    while subarray_len < length:
        # divide into smaller chunks (each of length subarray_len) and merge
        return_head = divide_list(return_head, subarray_len)
        # one level up
        subarray_len = subarray_len * 2

    return return_head.next


def divide_list(return_head, subarray_len):
    prev_head = return_head
    head = return_head.next

    while head:
        # get h1
        h1 = head
        i = subarray_len
        while i > 0 and head:
            head = head.next
            i -= 1

        # if i is still larger than 0, then h1 is the last group
        # no need to merge since h2 will be empty
        if i > 0:
            break

        # otherwise get h2 the same way
        h2 = head
        i = subarray_len
        while i > 0 and head:
            head = head.next
            i -= 1
        len_h1 = subarray_len

        # since h2 could be the last group (i > 0 after the while loop),
        # so its length could be smaller than subarray_len
        len_h2 = subarray_len - i

        # now merge h1 and h2
        # prev_head is the running head of the merged group
        # use lengths of the groups as the criterion to stop the loop:
        # can avoid breaking the group with the rest of the list
        while len_h1 and len_h2:
            if h1.val < h2.val:
                prev_head.next = h1
                h1 = h1.next
                # reduce the length of h1
                len_h1 -= 1
            else:
                prev_head.next = h2
                h2 = h2.next
                # reduce the length of h2
                len_h2 -= 1
            # advance prev_head by 1
            prev_head = prev_head.next

        # if len_h1 > 0, it means len_h2 == 0
        # append the rest of h1 (and remember h2 and the rest of the list is linked to h1)
        if len_h1 > 0:
            prev_head.next = h1
        # otherwise len_h2 must > 0
        else:
            prev_head.next = h2

        # now we have completed the merge part, advance the prev_head to the last number of the merged list
        # one of len_h1 and len_h2 must be positive, reduce to 0
        while len_h1 > 0 or len_h2 > 0:
            prev_head = prev_head.next
            len_h1 -= 1
            len_h2 -= 1

        # this is the most important line, it connect the last element of the merged list to the next group
        # we have updated head to be the first element of the next group (if any)
        # thus we can avoid of having an infinite loop (since h1 and h2 are linked all the way to the end)
        # we are essentially skipping the repeating part (where the loop will arise) and move on to the next group
        prev_head.next = head

    return return_head


test = list2ListNode([4, 5, 10, 2, 3, 6, 7, 9])
print(ListNode2list(sortList_bottom_up(test)))
