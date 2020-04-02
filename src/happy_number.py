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
        if res == 1:
            return True
        if res_dict.get(res):
            return False
        else:
            res_dict[res] = 1
            n = res


def breakdown(n):
    """
    (Helper) Break the n into non-negative integers less than 10
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


test = 19
print(isHappy(test))
