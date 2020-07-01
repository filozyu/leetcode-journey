def fizzBuzz(n):
    """
    Hard coding, judge for every possible condition
    Time: O(n)
    Space: O(1) not considering res
    """
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


def fizzBuzz_faster(n):
    """
    Using dictionary, to avoid multiple explicit conditions, and avoid judging repetitively
    Time: O(n)
    Space: O(1) not considering res and space for nums is constant
    """
    res = []
    nums = {3: "Fizz", 5: "Buzz"}
    for i in range(1, n + 1):
        this_str = ""
        for j in nums:
            if i % j == 0:
                this_str += nums[j]
        if this_str == "":
            res.append(str(i))
        else:
            res.append(this_str)
    return res
