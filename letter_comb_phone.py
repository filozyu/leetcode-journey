def letterCombinations_recursive(digits):
    """
    Recursion brute force (or DFS)
    Time: O(3^n + 4^m) n: number of {2:6, 8} in digits, m: number of {7, 9} in digits
    Space: O(3^n + 4^m) all possible combinations
    """
    if digits == "":
        return []
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    n = len(digits)
    if n == 1:
        return mapping[digits]
    else:
        # here the list structure (always take the elements that were added the latest)
        # implies a stack and hence can be viewed as DFS
        # get the existing combinations
        prev_list = letterCombinations_recursive(digits[:-1])
        curr_list = []
        # for each combinations
        for i in prev_list:
            # extend each combinations
            for j in mapping[digits[-1]]:
                curr_list.append(i + j)
        return curr_list


def letterCombinations_backtrack(digits):
    """
    Backtracking (sort of), with similar to recursion, due to the absence of rejection
    Time: O(3^n + 4^m) n: number of {2:6, 8} in digits, m: number of {7, 9} in digits
    Space: O(3^n + 4^m) all possible combinations
    """
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def backtrack(combination, next_digits):
        """
        Backtracking needs to have rejection and acceptance,
        here only acceptance is present, no rejection is needed

        CANDIDATE: combination
        Possible EXTENSIONS: next_digits
        """
        # ACCEPT: if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)

        # REJECTION criterion should go here if there is one

        # EXTEND the candidate: if there are still digits to check
        else:
            # the next available digit
            # FIRST: generate the first extension of combination.
            for letter in mapping[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                # NEXT: generate the next alternative extension of combination, after the first extension.
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output
