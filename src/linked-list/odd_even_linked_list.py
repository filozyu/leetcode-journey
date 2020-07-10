from utils import list2ListNode, ListNode2list


def oddEvenList(head):
    """
    Move odd nodes to the front
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head
    # last_odd points to the last node of the odd list
    last_odd = head
    # first_eve points to the first node of the even list
    # prev points to the node before the one we are processing (prev always points to an even node)
    prev = first_eve = head.next
    if prev:
        # curr points to the node we are processing (it always points to an odd node)
        # only process the list if there are more than two nodes
        curr = prev.next

        while curr:
            # get the next node (even)
            next_node = curr.next
            # link prev (even) to the next node (even), thus removing curr from its original position
            prev.next = next_node
            # link the whole even list after curr (odd)
            curr.next = first_eve
            # link curr to the end of the odd list
            last_odd.next = curr

            # two possibilities at the end of the list
            # 1) next_node is None (the whole list has odd number of nodes)
            #    then break from the loop and we are done
            #    which means curr (before we have processed it) is the last element of the whole list

            # 2) next_node is the last node in the list (the whole list has even number of nodes)
            #    enter the if block but curr will be updated to None
            #    which means the loop will stop as well

            if next_node:
                # curr is now the last node in the odd list
                last_odd = curr
                # go to the next ODD node (remember next_node is always even)
                curr = next_node.next
                # update prev (even)
                prev = next_node
            else:
                break
    return head


test = list2ListNode([1, 2, 3, 4, 5, 6, 7])
print(ListNode2list(oddEvenList(test)))
