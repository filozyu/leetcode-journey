# Two pointers, recursion
from utils import list2ListNode


def isPalindrome_recursion(head):
    """
    Recursion with two colliding pointers
    Time: O(n)
    Space: O(n), the recursion stack
    """

    def recursive(right):
        # the change on left should be reflected globally
        nonlocal left

        # in every recursive call, we move the right one step forward
        # until right is at the very last node in the list
        if right.next:
            is_same = recursive(right.next)

        # we enter this else block if right is the very last node
        else:
            # set is_same to True since we haven't compared yet
            is_same = True
        # the FIRST comparison in all recursive call will be
        # right at the right end
        # left at the left end
        # is_same is True
        # if the condition is matched,
        # left will move forward and when we are out of the inner most recursive call,
        # right will move backward as a result of getting back to the previous recursive call

        # However here left will move all the way to the right end
        # since the recursive call starts with right at the left end,
        # but this does not matter and can be avoided if we start to call the recursion when right is at the middle
        if is_same and right.val == left.val:
            left = left.next
            return True
        else:
            return False

    if not head:
        return True
    # initialise left
    left = head
    return recursive(head)


def isPalindrome(head):
    """
    In-place, one pass, constant space
    Reverse the second half of the list and compare it with the first half
    Time: O(n)
    Space: O(1)
    """

    def reverse_list(node):
        # reverse linked list
        if not node:
            return node
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    if not head:
        return True
    # first get to the middle point use two pointers
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # next find the head of the second half
    if fast:
        # the length of the list is odd, slow.next is the head of the second half
        second_head = slow.next
    else:
        # the length of the list is even, slow is the head of the second half
        second_head = slow
    # reverse the second half
    reversed_second_head = reverse_list(second_head)

    # compare the reversed second half with the whole list
    # (note that we are only comparing the first half of the whole list though)
    # After comparing all nodes in the reversed second half, head should be either
    # 1) at the head of the second half (even list)
    # 2) one node before the second half (odd list)
    while reversed_second_head:
        if head.val == reversed_second_head.val:
            head = head.next
            reversed_second_head = reversed_second_head.next
        else:
            return False
    return True


test = list2ListNode([1])
print(isPalindrome(test))
