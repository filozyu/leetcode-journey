from collections import Counter


def frequencySort(s):
    """
    Hash table and sorting
    Time: O(nlogn)
    Space: O(n)
    # NOTE: if we know that there are k <= n unique letters, then time complexity is O(n + klogk)
    # space complexity stays the same
    """
    # or use a Counter here then call most_common() for a faster solution
    freq_dict = {}
    for i in range(len(s)):
        if freq_dict.get(s[i]) is not None:
            freq_dict[s[i]] += 1
        else:
            freq_dict[s[i]] = 1
    char_freq_pair = list(freq_dict.items())
    char_freq_pair.sort(key=lambda x: x[1], reverse=True)

    # NOTE: one cannot use naive string appending, since strings are immutable
    # each time a new string is created and the appended results are copied into that new string
    # thus making the time complexity O(n^2) (n loops and in each loop the copy will be 1, ..., n)
    return "".join([c[0] * c[1] for c in char_freq_pair])


def frequencySort_bucket_sort(s):
    """
    Count dict and bucket sort
    Since the values to be sorted can only be from 1 to n
    Time: O(n)
    Space: O(n)
    """
    if len(s) < 1:
        return ""
    res_str = []
    freq_dict = Counter(s)
    max_val = max(freq_dict.values())
    buckets = [[] for _ in range(max_val + 1)]
    for c, f in freq_dict.most_common():
        buckets[f].append(c)

    for i in range(len(buckets) - 1, 0, -1):
        for c in buckets[i]:
            res_str.append(c * i)

    return "".join(res_str)


test = "tree"
print(frequencySort_bucket_sort(test))
