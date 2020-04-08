from utils import ListNode2list, list2ListNode


def reverseKGroup(head, k):
    """
    One pass
    Time: O(n)
    Space: O(1)
    e.g.
    [1,2,3,4,5,6,7], k = 3
    Within each group, update the head with the next node
    First group [1,2,3]->[2,1,3]->[3,2,1]
    link 1 to 4, set return_head to 3
    Second group [4,5,6]->[5,4,6]->[6,5,4]
    link 6 to 1, link 7 to 4
    final output: [3,2,1,6,5,4,7]

    """
    # if k = 1, no reversion needed
    if k <= 1:
        return head
    # get the length first
    length = 0
    curr_node = head
    while curr_node:
        length += 1
        curr_node = curr_node.next
    # get the number of groups
    n_groups = length // k
    # set the tail of the first group
    group_tail = head
    # initialise the tail of the previous group
    prev_group_tail = None
    # initialise the head for return
    return_head = None
    # reverse within each group
    for i in range(n_groups):
        # the following will take care of reversing the current group:
        # in every group, temp_head is initialised as the first node in the unaltered group
        temp_head = group_tail
        # and temp_rest is initialised as the second node in the unaltered group
        temp_rest = group_tail.next
        # this will prevent a loop in nodes
        group_tail.next = None
        # since the first node in the group are already reversed, loop for the rest k-1 nodes
        for j in range(k - 1):
            # save the current head as prev_head
            prev_head = temp_head
            # update the current head to be the next node in the unaltered part of the group
            # i.e. at each step, update the head as the first unaltered node
            temp_head = temp_rest
            # update temp_rest to be the rest of the unaltered nodes in the group
            temp_rest = temp_rest.next
            # link the current head to the previous head
            temp_head.next = prev_head
        # after the entire group has been reversed, set group_head to be temp_head
        group_head = temp_head

        # the following will take care of linking different groups
        if not prev_group_tail:
            # this will only be called in the first group
            prev_group_tail = group_tail
            # return head is set as the head of the first group, and will not be changed
            return_head = group_head
        else:
            # this will be called for all groups but the first one
            # link this group to the previous tail
            prev_group_tail.next = group_head
            # update the previous group tail to the current tail
            prev_group_tail = group_tail
        # link the rest of the list to the latest group's tail (in case we are at the last group)
        group_tail.next = temp_rest
        # temp_rest is the first element in the next group, which should be the tail once reversed
        group_tail = temp_rest

    return return_head


def reverseKGroup_stack(head, k):
    """
    One pass stack
    Time: O(n)
    Space: O(1)
    This approach is very similar to the above one, only using stack to reverse each group
    """
    # trivial case and get length
    if k <= 1:
        return head
    length = 0
    curr_node = head
    while curr_node:
        length += 1
        curr_node = curr_node.next
    # initialise
    n_groups = length // k
    curr_node = head
    prev_tail = None
    return_head = None
    # loop for each group
    for i in range(n_groups):
        stack = []
        while len(stack) < k:
            stack.append(curr_node)
            curr_node = curr_node.next
        # the one added the latest is the new head
        group_head = stack.pop()
        prev_node = group_head
        # save the next group
        next_group = group_head.next
        # loop until stack is empty
        while stack:
            curr_node = stack.pop()
            prev_node.next = curr_node
            prev_node = curr_node
        # now curr_node is the tail of the group (whose next is still the penultimate node, therefore a loop)
        # to break the loop, reset the next to next_group, note that cannot reset to None
        # since if this is the final group, then curr_node.next should point to the remaining nodes in the list
        curr_node.next = next_group
        # similar as above
        if i == 0:
            prev_tail = curr_node
            return_head = group_head
        else:
            prev_tail.next = group_head
            prev_tail = curr_node
        # similarly, update group tail to the next group
        curr_node = next_group
    return return_head


test = list2ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ListNode2list(reverseKGroup_stack(test, 3)))
