# BFS, directed graph, roots tracing
from collections import deque


def dependency_graph(words):
    """
    Helper function to build the graph
    Time: O(C) C is the sum of lengths of strings in words
    Space: O(1) or more precisely: O(U + E)

    U is the number of unique characters in words
    E is the number of edges in the graph

    E = min(U^2, N) in the worst case, N is the number of words. But since U <= 26, we can say O(U + E) is O(1)

    Derivation:
    E must be smaller than N - 1 since that's the number of relationships we can derive from words
    E also has to be smaller than U^2 since that's the number of edges in a complete graph with U nodes
    """
    # construct the adjacency list and the in-degree list for every unique character in the dictionary
    # Note: adj_list only contains outgoing edges, in_degree only counts incoming edges
    adj_list = {}
    in_degree = {}
    # Time: O(C)
    for word in words:
        for c in word:
            adj_list[c] = set()
            in_degree[c] = 0

    # add neighbours and in-degree for every pair of words
    # Time: O(C) loop through the words and for every pair of words, loop through all the characters (worst case)
    for i in range(len(words) - 1):
        curr_word = words[i]
        next_word = words[i + 1]

        k = 0
        min_len = min(len(curr_word), len(next_word))
        while k < min_len:
            if curr_word[k] != next_word[k]:
                # we have not recorded this edge
                if next_word[k] not in adj_list[curr_word[k]]:
                    # add to adjacency list of the parent character
                    adj_list[curr_word[k]].add(next_word[k])
                    # increment the in-degree of the child character
                    in_degree[next_word[k]] += 1
                k += 1
                break
            else:
                k += 1

            if k == min_len and len(curr_word) > len(next_word):
                # here we have the empty character being preceded by some actual character, dictionary is invalid
                return {}, {}

    return adj_list, in_degree


def alienOrder(words):
    """
    BFS in directed graph, with root removing
    Time: O(C) since C > N so O(C) is the dominating term
    Space: O(1) or more precisely: O(U + E), E = min(U^2, N)
    """
    # Time: O(C), Space: O(1)
    adj_list, in_degree = dependency_graph(words)
    if adj_list or in_degree:
        order = []
        # get all the "roots"
        # Time: O(U)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        # Time: BFS has O(V + E) = O(U + min(U^2, N))
        # A node is visited once ALL its incoming edges are visited (unlike conventional BFS)
        while queue:
            # every character in popped from queue is ready to be joined to the order
            c = queue.popleft()
            order.append(c)
            # for all immediate characters after the roots
            for n in adj_list[c]:
                # since roots has been added ("removed" from the graph), all in degree will decrement 1
                in_degree[n] -= 1

                if in_degree[n] == 0:
                    # these are the new roots now, enqueue them
                    queue.append(n)

        # this means we have a cycle in the graph,
        # so at a point there is no root and the remaining nodes all have in-degree larger than 0
        if len(order) < len(in_degree):
            return ""

        return "".join(order)

    # this is when the empty character is preceded by any character
    # (e.g. "operate" precedes "opera" in English, which is lexicographically incorrect)
    else:
        return ""


# test = ["wrt", "wrf", "er", "ett", "rftt"]
# test = ["z","z"]
test = ["ab", "adc"]
print(alienOrder(test))
