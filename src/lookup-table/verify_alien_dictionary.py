# Hash table
def isAlienSorted(words, order):
    """
    Check adjacent words
    Time: O(nk) in worst case, n - number of words, k - average (or maximal) length of a word
    Space: O(1)
    """
    dict_order = {}
    for i in range(len(order)):
        # create a dictionary recording the order of the characters
        dict_order[order[i]] = i

    for j in range(len(words) - 1):
        # check two words at a time
        curr_word = words[j]
        next_word = words[j + 1]

        min_len = min(len(curr_word), len(next_word))

        k = 0
        while k <= min_len - 1:
            if dict_order[next_word[k]] < dict_order[curr_word[k]]:
                return False
            # if satisfied, no need to compare this two words, go to the next pair
            elif dict_order[next_word[k]] > dict_order[curr_word[k]]:
                break
            # k only increments if the previous letters are the same for both words
            else:
                k += 1

        # if next word is a subset of the current word, this does not satisfy the lexicography order
        if k == min_len and len(curr_word) > len(next_word):
            return False

    return True


test_words = ["hello", "leetcode"]
test_order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(test_words, test_order))
