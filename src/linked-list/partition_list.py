from utils import list2ListNode, ListNode2list


def partition(head, x):
    """
    Add nodes to two list (depending on the node being greater than x and smaller than x)
    Time: O(n)
    Space: O(1) (all nodes are from the original list)
    """
    # initialise the heads and tails of the two lists
    g_head, g_last = None, None
    l_head, l_last = None, None
    # curr is the node we will be working with in each iteration
    curr = head

    while curr:

        # put curr to the greater_list
        if curr.val >= x:
            # if head is empty then curr is the first node (and the last node)
            if not g_head:
                g_head = curr
                g_last = curr
            # otherwise we can update normally
            else:
                assert(g_last is not None)
                # append curr to the list
                g_last.next = curr
                # curr is now the new tail
                g_last = curr

        # put curr to the less_list
        else:
            if not l_head:
                l_head = curr
                l_last = curr
            else:
                assert(l_last is not None)
                l_last.next = curr
                l_last = curr

        # advance curr by one step
        curr = curr.next

    # if the greater_list is not empty
    if g_head:
        # cut whatever is behind the tail of the greater_list
        g_last.next = None

    # if the less_list is not empty, append it to the left of the greater_list
    if l_head:
        l_last.next = g_head
        return l_head
    # otherwise there is no nodes less than x in the linked list
    else:
        return g_head


test = list2ListNode([1, 4, 3, 2, 5, 2])
test_x = 3
print(ListNode2list(partition(test, test_x)))
