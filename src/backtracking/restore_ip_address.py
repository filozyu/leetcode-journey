def restoreIpAddresses(s):
    """
    Backtracking
    Time: O(1) since backtrack only considers at most the first 12 digits in s
    Space: O(1) size of curr_res is constant (4), so is the recursion stack
    """
    res = []

    def backtrack(start, curr_res):
        # exit if we have used all s and ended up with four numbers
        if len(curr_res) == 4 and start == len(s):
            res.append(".".join(curr_res[:]))

        # each number can consists of 1 to 3 digits (range from 0 to 255)
        # note we do not need to check whether start + 3 <= len(s)
        # since the slicing below will stop when reaching the end
        for i in range(start, start+3):
            next_part = s[start: i + 1]
            # stop if the sliced part is None or the number is above 255
            if next_part == "" or int(next_part) > 255:
                break

            # stop if the sliced part contains more than 1 digit and the the first digit is 0
            if len(next_part) > 1 and next_part[0] == "0":
                break

            # stop if the length is already 4 (in this case start != len(s))
            if len(curr_res) >= 4:
                break

            curr_res.append(next_part)
            backtrack(i + 1, curr_res)
            curr_res.pop()

    backtrack(0, [])

    return res


test = "010010"
print(restoreIpAddresses(test))
