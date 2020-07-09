from utils import list2ListNode, ListNode2list, ListNode


def insertionSortList_built_in_sort(head):
    """
    (Not with constant space, and not insertion sort)
    Time: O(nlogn)
    Space: O(n)
    """
    if not head:
        return head
    res_list = []
    while head:
        res_list.append(head)
        head = head.next
    res_list.sort(key=lambda x: x.val)
    return_head = ListNode(0)
    head = res_list[0]
    return_head.next = head
    for i in range(1, len(res_list)):
        head.next = res_list[i]
        if i == len(res_list) - 1:
            head.next.next = None
        else:
            head = res_list[i]
    return return_head.next


def insertionSortList_concise(head):
    """
    Maintain a sorted list in return_head and insert nodes from the unsorted list one by one
    Time: O(n^2)
    Space: O(1) ?
    """
    if not head:
        return None
    # return_head is empty (apart from the dummy head) first, and will be used to store sorted nodes
    return_head = ListNode(-1)
    # curr_node is the node that will be inserted
    curr_node = head
    # curr_node will be inserted between prev_node and prev_node.next
    prev_node = return_head

    while curr_node:
        next_node = curr_node.next
        # locate where to insert (advancing prev_node) from the start of the sorted list
        while prev_node.next is not None and prev_node.next.val < curr_node.val:
            prev_node = prev_node.next
        # insert curr_node between prev_node and prev_node.next
        # since prev_node.val < curr_node.val <= prev_node.next.val
        # prev_node.next is now connected after curr_node
        curr_node.next = prev_node.next
        # and curr_node is connected after prev_node
        prev_node.next = curr_node
        # reset prev_node to be the start of the sorted list
        prev_node = return_head
        # choose the next unsorted node
        curr_node = next_node
    return return_head.next


def insertionSortList(head):
    """
    Use the same list to store the sorted and the unsorted nodes,
    take one node out from the unsorted part once at a time and insert it to the sorted part,
    by scanning from the start of the sorted part
    Time: O(n^2)
    Space: O(1)
    """
    if not head or not head.next:
        return head

    return_head = ListNode(-1)
    return_head.next = head
    curr_node = head.next
    # prev_node is the last node of the sorted list (the largest in the sorted list)
    prev_node = head

    while curr_node:
        # if curr_node is already larger than the last of the sorted node (prev_node)
        # then we don't need to move curr_node, simply increment the sorted list by one node
        if curr_node.val >= prev_node.val:
            prev_node = curr_node
            curr_node = curr_node.next
            continue
        # otherwise, curr_node is not immediately sorted as above
        # take curr_node out of the list
        prev_node.next = curr_node.next
        # insert curr_node to the sorted part by scanning from the start
        p = return_head
        while p.next.val <= curr_node.val:
            p = p.next
        # stop until p.val < curr_node.val < p.next.val
        # insert curr_node between p and p.next
        curr_node.next = p.next
        p.next = curr_node
        # get the next unsorted node
        curr_node = prev_node.next

    return return_head.next


test = list2ListNode([1, 5, 3, 4, 0])
print(
    ListNode2list(
        insertionSortList(test)
    )
)

