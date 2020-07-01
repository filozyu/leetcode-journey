def backspaceCompare(S, T):
    new_s = []
    for i in range(len(S)):
        if S[i] == "#":
            if len(new_s) > 0:
                new_s.pop()
            else:
                continue
        else:
            new_s.append(S[i])
    new_t = []
    for j in range(len(T)):
        if T[j] == "#":
            if len(new_t) > 0:
                new_t.pop()
            else:
                continue
        else:
            new_t.append(T[j])
    return new_s == new_t


def backspaceCompare_two_pointers_1(S, T):
    """
    Cumbersome two pointers
    Time: O(max(s, t)) s: len(S); t: len(T) or O(s+t) since it is O(2*max(s,t)), they are of the same order
    Space: O(1)
    """
    s_skip, t_skip = 0, 0
    # loop backward
    s_pointer, t_pointer = len(S) - 1, len(T) - 1
    while s_pointer >= 0 or t_pointer >= 0:
        # if there are unchecked char in S
        if s_pointer >= 0:
            # skip + 1, move to the next
            if S[s_pointer] == "#":
                s_skip += 1
                s_pointer -= 1
            # if not "#", but skip>0, skip this char
            elif S[s_pointer] != "#" and s_skip != 0:
                s_skip -= 1
                s_pointer -= 1
            # if not "#" and should not be skipped, but T is all checked, then not matching
            elif t_pointer < 0:
                return False
        if t_pointer >= 0:
            if T[t_pointer] == "#":
                t_skip += 1
                t_pointer -= 1
            elif T[t_pointer] != "#" and t_skip != 0:
                t_skip -= 1
                t_pointer -= 1
            elif s_pointer < 0:
                return False
        # if both S and T have unchecked elements and not to skip, check them
        if s_pointer >= 0 and t_pointer >= 0 and s_skip == 0 and t_skip == 0:
            # do not check if one of the chars is "#"
            if S[s_pointer] == "#" or T[t_pointer] == "#":
                continue
            # check if match
            match = S[s_pointer] == T[t_pointer]
            if not match:
                return False
            else:
                # if matched, move to the left
                s_pointer -= 1
                t_pointer -= 1
        # if one of S and T has been fully checked, and the other has elements left unskipped
        # continue to the next loop
        if (s_pointer < 0 or t_pointer < 0) and s_pointer != t_pointer:
            continue
    return True


def backspaceCompare_two_pointers_2(S, T):
    """
    Two pointers (concise)
    Time: O(s+t)
    Space: O(1)
    """
    from itertools import zip_longest

    def backward(strings):
        skip = 0
        for x in reversed(strings):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                # return iterables
                yield x
    # zip_longest example: a = [1, 2, 3, 4], b = [5, 6]
    # then [(x, y) for x, y in zip_longest(a, b)] is [(1, 5), (2, 6), (3, None), (4, None)]
    return all(x == y for x, y in zip_longest(backward(S), backward(T)))


# test_S = "y#fo##f"
# test_T = "y#fx#o##f"

# test_S = "ab##"
# test_T = "c#d#"

test_S = "isfcow#"
test_T = "isfcog#w#"

print(backspaceCompare_two_pointers_2(test_S, test_T))
