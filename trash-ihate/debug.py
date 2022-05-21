from collections import Counter


def checkAlmostEquivalent(word1, word2):
    word1_dict = Counter(word1)
    word2_dict = Counter(word2)

    for w1 in word1_dict:
        if w1 in word2_dict:
            if abs(word1_dict[w1] - word2_dict[w1]) > 3:
                return False
        else:
            return False
    return True


print(checkAlmostEquivalent("zzzyyy", "iiiiii"))
