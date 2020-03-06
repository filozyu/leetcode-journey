# Q3
# Given a string, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
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
