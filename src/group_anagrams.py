from collections import defaultdict, Counter


def groupAnagrams(strs):
    """
    Hacking (slow)
    Time: O(nk), n: length of strs; k: max length of words;
    Space: O(nk), same as strs
    """
    res_dict = defaultdict(list)
    for word in strs:
        key = frozenset(Counter(word).items())
        res_dict[key].append(word)
    return res_dict.values()


def groupAnagrams_sorted_str(strs):
    """
    Sorted string (fast)
    Time: O(nklogk), n: length of strs; k: max length of words; klogk for sorting
    Space: O(nk), same as strs
    """
    res_dict = defaultdict(list)
    for word in strs:
        # list is unhashable
        res_dict[tuple(sorted(word))].append(word)
    return res_dict.values()


def groupAnagrams_count(strs):
    """
    Counting letters
    Time: O(nk), n: length of strs; k: max length of words
    Space: O(nk), same as strs
    """
    res_dict = defaultdict(list)
    for word in strs:
        # count for each letter in alphabet
        count = [0] * 26
        for char in word:
            # ord() return the Unicode integer representing the character
            # therefore ord("b") - ord("a") = 1
            # ord("z") - ord("a") = 25 etc.
            count[ord(char) - ord("a")] += 1
        res_dict[tuple(count)] = word
    return res_dict.values()


test = [
    "hos","boo","nay","deb","wow","bop","bob","brr","hey","rye",
    "eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod",
    "aha","nam","gap","yea","doc","pen","job","dis","max","oho",
    "jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog",
    "let","gym","bye","lon","aft","eel","sol","jab"
]

print(groupAnagrams(test))
