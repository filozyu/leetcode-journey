# Shortest paths, BFS
from collections import defaultdict, deque


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


def BFS_shortest_path(beginWord, endWord, word2abb, abb2word):

    curr_level = defaultdict(list)
    que = deque([beginWord])
    visited = set()

    # curr_level and next_level records the paths
    curr_level[beginWord] = [[beginWord]]

    while que:
        next_level = defaultdict(list)
        curr_level_len = len(que)
        # loop through the current level
        for i in range(curr_level_len):
            curr_node = que.popleft()
            if curr_node not in visited:
                visited.add(curr_node)

            if curr_level.get(endWord) is not None:
                return curr_level[endWord]

            neighbours = []
            # the for loop below will run k times
            for abb in word2abb[curr_node]:
                # the for loop below wil run at most 26 times
                for n in abb2word[abb]:
                    # checking in set is O(1)
                    if n not in visited:
                        visited.add(n)
                        neighbours.append(n)
                    if curr_level.get(curr_node) is not None:
                        for curr_path in curr_level[curr_node]:
                            next_level[n].append(curr_path + [n])

            que += neighbours

        curr_level = next_level

    return []


def findLadders(beginWord, endWord, wordList):
    word2abb, abb2word = getDict(beginWord, wordList)
    return BFS_shortest_path(beginWord, endWord, word2abb, abb2word)


def findLadders_alt(beginWord, endWord, wordList):
    """
    Rather odd
    Time: O(n * k^2 * p) (?)
    n the number of words, k the length of a single word, p the average number of paths (all layers)
    Space: O(n + ?) ? is curr_level and next_level
    """

    # turning a set to a list: O(n)
    word_dict = set(wordList)

    if endWord not in word_dict:
        return []

    # we only keep two levels at a time,
    # each level is a dictionary that maps node at that level to a list of shortest paths that ends with that node
    # the level is relative to the root (beginWord)

    # curr_level[node] contains all the shortest paths from beginWord and end with node
    curr_level = defaultdict(list)
    # initialisation: the first level only contains the root, and to get to root, there is only one path (itself)
    curr_level[beginWord] = [[beginWord]]

    # the while loop combined with the for loop (in curr_level) will run for n times (total number of words)
    # in the last iteration, next_level will not be updated thus resulting curr_level being empty
    while curr_level:
        # define the next level, which will be constructed in this loop
        next_level = defaultdict(list)

        # loop through all the keys (i.e. nodes at the current level, level starts counting from beginWord)
        # NOTE: since we are looping from the left, and we append the neighbours of curr_node in a separate dict
        # this is effectively a queue, where curr_level will eventually contain all the popped nodes at this level
        # and next_level will contain all the added nodes at next level

        for curr_node in curr_level:
            # note that curr_level is already defined in the previous loop
            # so if we have already added endWord in the previous loop, we can extract it and return all the paths
            if curr_node == endWord:
                return curr_level[endWord]
            # loop through all the unvisited neighbours of curr_node
            # the outer loop runs k times (length of a word)
            for i in range(len(curr_node)):
                # this inner loop will run 26 times
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # slicing will run k times
                    new_word = curr_node[:i] + c + curr_node[i + 1 :]
                    # if condition will be O(1), note that word_dict gets update in the while loop
                    # so it only contains unvisited nodes
                    if new_word in word_dict:
                        # the runtime of the following operation depends on the number of paths to curr_node
                        # depends on the structure of the graph, but say on average it will run p times
                        next_level[new_word] += [
                            path + [new_word] for path in curr_level[curr_node]
                        ]
        # remove the visited nodes from word_dict
        word_dict -= set(next_level.keys())
        # update curr_level, effectively removing all the popped nodes from the current level
        curr_level = next_level

    return []


test = ["hot", "dot", "dog", "lot", "log", "cog"]
test_start = "hit"
test_end = "cog"
print(findLadders_alt(test_start, test_end, test))
