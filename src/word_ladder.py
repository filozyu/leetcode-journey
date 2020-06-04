from collections import defaultdict, deque


def ladderLength_BFS(beginWord, endWord, wordList):
    """
    BFS and slow graph construction
    Time: O(kn^2) the predominant term in constructing the graph
    Space: O(2ek) e - number of edges in the graph, 2e is always greater than n; this is considering char, not str
    """
    # graph construction
    visited = []
    adj_dict = defaultdict(set)
    if endWord not in wordList:
        return 0
    for i in range(len(wordList)):
        if sum([wordList[i][k] != beginWord[k] for k in range(len(beginWord))]) == 1:
            adj_dict[beginWord].add(wordList[i])
            adj_dict[wordList[i]].add(beginWord)
        for j in range(i, len(wordList)):
            if (
                sum([wordList[i][k] != wordList[j][k] for k in range(len(beginWord))])
                == 1
            ):
                adj_dict[wordList[j]].add(wordList[i])
                adj_dict[wordList[i]].add(wordList[j])

    # BFS part
    queue = deque()
    queue.append("NEW_LEVEL")
    queue.append(beginWord)
    visited.append(beginWord)
    dist = 0
    while queue:
        curr_node = queue.popleft()
        if curr_node == endWord:
            return dist
        if curr_node == "NEW_LEVEL":
            if len(queue) >= 1:
                dist += 1
                queue.append("NEW_LEVEL")
                continue
            else:
                return 0
        neighbours = []
        for n in adj_dict[curr_node]:
            if n not in visited:
                visited.append(n)
                neighbours.append(n)

        queue += neighbours

    return 0


def getDict(beginWord, wordList):
    """
    build word2abb and abb2word dicts
    word2abb - "bit": "*it", "b*t", "bi*"
    abb2word - "b*t": "bit", "bot", "but", ...
    Time: O(nk^2) n - number of words, k - length of a word
    Space: O(nk^2) NOTE: original wordList is of space O(nk) as by the number of char, not str
    """
    word2abb = defaultdict(list)
    abb2word = defaultdict(list)
    if beginWord not in wordList:
        wordList.append(beginWord)
    # this loop runs n times
    for w in wordList:
        # this loop runs k times
        for i in range(len(w)):
            # slicing strings: O(k)
            # in word2abb, number of abb for each word: k, each word length: k; so num of char: k^2
            # in abb2word, space will be smaller than word2abb since each abb can hold at most 26 words,
            # thus the space (num of char) for each abb is 26k
            word2abb[w].append(w[:i] + "*" + w[i + 1 :])
            abb2word[w[:i] + "*" + w[i + 1 :]].append(w)

    return word2abb, abb2word


def BFS(start, end, word2abb, abb2word):
    """
    BFS using word2abb and abb2word
    Time: O(nk)
    Space: O(nk) if counting chars, rather than strs
    """
    visited = set()
    queue = deque()
    # add level indicator
    queue.append("NEW_LEVEL")
    queue.append(start)
    visited.add(start)
    dist = 0
    # this while loop will run at most n times
    while queue:
        curr_node = queue.popleft()
        if curr_node == end:
            return dist
        # if a new level is reached (depth + 1)
        if curr_node == "NEW_LEVEL":
            if len(queue) >= 1:
                dist += 1
                queue.append("NEW_LEVEL")
                continue
            else:
                return 0
        neighbours = []
        # the for loop below will run k times
        for abb in word2abb[curr_node]:
            # the for loop below wil run at most 26 times
            for n in abb2word[abb]:
                # checking in set is O(1)
                if n not in visited:
                    visited.add(n)
                    neighbours.append(n)

        queue += neighbours
    return 0


def ladderLength_BFS_fast(beginWord, endWord, wordList):
    """
    BFS with faster graph construction (by using word2abb and abb2word dicts)
    Time: O(nk^2)
    Space: O(nk^2)
    """
    word2abb, abb2word = getDict(beginWord, wordList)
    return BFS(beginWord, endWord, word2abb, abb2word)


test_b = "hit"
test_e = "cog"
test_w = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladderLength_BFS_fast(test_b, test_e, test_w))
