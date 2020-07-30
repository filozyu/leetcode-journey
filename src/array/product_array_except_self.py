def productExceptSelf(nums):
    """
    Left and right product list
    Time: O(n)
    Space: O(n) (even if output is not counted)
    """
    left_prod, right_prod = [nums[0]], [nums[-1]]
    for i in range(1, len(nums)):
        left_prod.append(left_prod[-1]*nums[i])
    for j in range(len(nums)-2, -1, -1):
        right_prod.append(right_prod[-1]*nums[j])
    output = []

    for k in range(0, len(nums)):
        if k == 0:
            output.append(right_prod[len(nums)-2])
        elif k == len(nums) - 1:
            output.append(left_prod[len(nums)-2])
        else:
            output.append(left_prod[k-1] * right_prod[len(nums)-2-k])
    return output


def productExceptSelf_log(nums):
    """
    Logarithm, cannot handle negative numbers (therefore INCORRECT)
    Time: O(n)
    Space: O(1) (excluding the return array, which itself is O(n))
    """
    from math import exp, log
    log_sum = 0
    zero_count = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count.append(i)
            if len(zero_count) == 2:
                return [0]*len(nums)
        else:
            log_sum += log(nums[i])
    if len(zero_count) == 1:
        out = [0]*len(nums)
        out[zero_count[0]] = round(exp(log_sum))
        return out
    else:
        return [round(exp(log_sum - log(i))) for i in nums]


test = [1,0,3,4]
print(productExceptSelf_log(test))
