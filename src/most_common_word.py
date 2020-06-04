from collections import Counter
import re
import string


def mostCommonWord(paragraph, banned):
    # regex = re.compile('[%s]' % re.escape(string.punctuation))
    word_list = re.sub(r"[^\w\s]", " ", paragraph).lower().split(" ")
    # word_list = regex.sub(' ', paragraph).lower().split(" ")
    mc = Counter(word_list).most_common()
    for word in mc:
        if word[0] != "" and word[0] not in banned:
            return word[0]
    return -1


test = "a, a, a, a, b,b,b,c, c"
test_ban = ["a"]
print(mostCommonWord(test, test_ban))
