from collections import Counter, defaultdict
import heapq


def topKFrequent(words, k):
    """
    Two dictionaries
    Time: O(kn) ?
    Space: O(n) for word_count_dict
    """
    word_count_dict = {}
    count_word_dict = defaultdict(list)
    for word in words:
        if word_count_dict.get(word):
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    counts = sorted(list(word_count_dict.values()))
    counts = sorted(list(set(counts[-k:])), reverse=True)
    for count in counts:
        for word in word_count_dict:
            if word_count_dict[word] == count:
                count_word_dict[count].append(word)

    res_list = []
    for count in count_word_dict:
        res_list += sorted(count_word_dict[count])
    if k < counts[0]:
        return res_list[:k]
    else:
        return res_list


def topKFrequent_counter(words, k):
    """
    Using counter
    Time: O(nlogn)
    Space: O(n)
    """
    # count will take O(n)
    count = Counter(words)
    candidates = list(count.keys())
    # sort will take O(nlogn)
    # key in sorting: a function, and the results will be sorted by the output
    # To sort a list of tuples, first sort the first element in tuples,
    # then compare the second elements whose first elements are the same, and so on
    # below the first (priority) is the word count, the larger the better;
    # the second is the word itself, where we prefer smaller words (alphabetical order) when there is a tie
    candidates.sort(key=lambda x: (-count[x], x))
    return candidates[:k]


def topKFrequent_counter_heap(words, k):
    """
    Counter with heap
    Time: O(n + klogn) - n for counting and heapify, klogn for pop out k nodes
    Space: O(n), count and heap
    """
    count = Counter(words)
    # freq: the larger it is, the closer to the top the pair is in the heap
    # word: when freq is the same, the smaller it is, the closer to the top the pair is in the heap
    heap = [(-freq, word) for word, freq in count.items()]
    # build a heap from the list: O(n)
    heapq.heapify(heap)
    # heappop(heap) will return the top (word, freq) pair of the heap
    # and we only want the word
    # each pop: O(logn) (this is also the time for push), since after popping out the smallest element,
    # the rest of the heap needs to be readjusted to satisfy the conditions of a heap (i.e. children > parent)
    res = [heapq.heappop(heap)[1] for _ in range(k)]
    return res


test = ["i", "love", "leetcode", "i", "love", "coding"]
test_k = 2
print(topKFrequent_counter_heap(test, test_k))
