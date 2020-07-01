def isHappy(n):
    """
    Brute force
    Time: ???
    Space: ???
    """
    res_dict = {}
    while True:
        curr_list = breakdown(n)
        res = 0
        for i in curr_list:
            res += i ** 2
        # OR use get_sum
        # res = get_sum(n)
        if res == 1:
            return True
        if res_dict.get(res):
            return False
        else:
            res_dict[res] = 1
            n = res


def breakdown(n):
    """
    (Helper) Break n into non-negative integers less than 10
    Time: O(log_{10}^{n})
    Space: O(log_{10}^{n})
    """
    res = []
    i = 10
    while True:
        curr = n % i
        res.append(int(10 * curr / i))
        n -= curr
        if n == 0:
            break
        i *= 10
    return res


def get_sum(n):
    """
    (Helper) Similar to breakdown but faster and return the sum directly
    Time: O(log_{10}^{n})
    Space: O(1)
    """
    res = 0
    while n != 0:
        # divmod(n, 10) returns n // 10 and n % 10
        n, digit = divmod(n, 10)
        res += digit ** 2
    return res


def isHappy_cycle(n):
    """
    Cycle detection with two pointers (Floyd's cycle-finding algorithm)
    Time: ???
    Space: O(1)
    """
    # Floyd's cycle-finding: hare (fast) and tortoise (slow)
    # underlying assumption is that the next number in the sequence is solely dependent on the previous number
    # which is the case in happy number
    # Also due to that every number will either stay at 1 or end up in a loop forever (only one loop starting from 4)
    # This algorithm can identify if there is a loop with constant extra space
    # Idea is in a sequence A_0, ..., A_a, A_a+1, ..., A_a+lambda where a denotes the starting point of the loop
    # and lambda denotes the minimum positive period of the loop
    # If A_i = A_j, (j>i) then i and j must both be in the loop and greater equal than a (see the underlying assumption)
    # therefore j = i + k * lambda, k a positive integer
    # So if we can find pattern like A_i = A_i+k*lambda, then we can confirm there is a loop
    # But k*lambda is unknown to us, however if we set i = k*lambda, then we only need to find A_i = A_2*i
    # Therefore we set the fast pointer to always have twice the distance as the slow pointer:
    # once the two equaled and say are x steps in the loop: A_a+x = A_a+x + a+x, where a+x = k*lambda
    slow = get_sum(n)
    fast = get_sum(slow)

    while fast != slow and fast != 1:
        # every time slow advance one step and fast advance two steps
        # so fast always covers twice the distance of that covered by slow
        slow = get_sum(slow)
        fast = get_sum(get_sum(fast))
        # if fast reached 1, end the update and return True
        # Otherwise, if fast and slow meet, meaning there is a loop and fast cannot be 1,
        # end the update and return False
    return fast == 1


test = 19
print(isHappy_cycle(test))
