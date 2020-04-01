def singleNumber(nums):
    """
    XOR
    Time: O(n)
    Space: O(1)
    """
    res = 0
    for i in nums:
        # ^: XOR (binary operation)
        # e.g. 3 ^ 2 = 1
        # since 11 ^ 10 = 01
        # In general:
        # A ^ 0 = A
        # A ^ A = 0
        # (A ^ B) ^ C = A ^ (B ^ C)
        # since all numbers appear exactly twice save one number appears only once,
        # all the non-single numbers will be cancelled out in pairs, leaves the very single one
        res = i ^ res
    return res
