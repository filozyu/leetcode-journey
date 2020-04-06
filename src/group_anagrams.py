from collections import defaultdict, Counter


def groupAnagrams(strs):
    res_dict = defaultdict(list)
    for word in strs:
        key = frozenset(Counter(word).items())
        res_dict[key].append(word)
    return res_dict.values()


test = [
    "hos","boo","nay","deb","wow","bop","bob","brr","hey","rye",
    "eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod",
    "aha","nam","gap","yea","doc","pen","job","dis","max","oho",
    "jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog",
    "let","gym","bye","lon","aft","eel","sol","jab"
]

print(groupAnagrams(test))
