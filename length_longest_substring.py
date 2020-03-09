# Q3
# Given a string, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring_one(s):
    """
    Brute force

    Time: O(n^2)
    Space: O(n^2) (worst)
    """
    if len(s) > 0:
        max_length = 1
    else:
        max_length = 0
    for i in range(len(s)):
        curr_list = [s[i]]
        if i + 1 < len(s):
            for j in range(i + 1, len(s)):
                if s[j] in curr_list:
                    if max_length < len(curr_list):
                        max_length = len(curr_list)
                        break
                    else:
                        break
                else:
                    curr_list.append(s[j])
            if max_length < len(curr_list):
                max_length = len(curr_list)
    return max_length


def lengthOfLongestSubstring_two(s):
    """
    Sliding window

    Time: O(n), assuming lookup key in dict using dict.get() is O(1)
    Space: O(n), for storing the lookup dict
    """
    max_len = 0
    start = end = 0
    lookup = {}
    for i in range(len(s)):
        end += 1
        if lookup.get(s[i]) and lookup[s[i]][-1] >= start:
            # found a repeated element
            start = lookup[s[i]][-1] + 1
            # reset start to be the next element of the repeated element
            lookup[s[i]].append(i)
            # update the location dict
        else:
            lookup[s[i]] = [i]
        if (end - start) > max_len:
            max_len = end - start
    return max_len
