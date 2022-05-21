def frequncySort(s):
    alphabate_arr = [0] * 60

    res = ""

    # Storing all elements count in arr
    for c in s:
        if c.isupper():
            alphabate_arr[ord(c) - 65 + 36] = alphabate_arr[ord(c) - 65 + 26] + 1
        elif c.islower():
            alphabate_arr[ord(c) - 97 + 10] = alphabate_arr[ord(c) - 97 + 10] + 1
        else:
            alphabate_arr[ord(c) - 48] = alphabate_arr[ord(c) - 48] + 1

    largest = -1
    key = -1
    while len(s) != len(res):
        for i in range(len(alphabate_arr)):
            if alphabate_arr[i] > largest:
                largest = alphabate_arr[i]
                key = i
        alphabate_arr[key] = -1

        if key > 25:
            res += chr(key + 65 - 26) * largest
        elif key > 9:
            res += chr(key + 97 - 10) * largest
        else:
            res += chr(key + 48) * largest

        largest = -1

    return res


def topKFrequent(words, key_el):
    d_words = Counter(sorted(words))
    sorted_d_words = [
        x for x in sorted(d_words, key=lambda x: d_words[x], reverse=True)
    ]
    print(sorted_d_words)
    res = []
    for el in sorted_d_words:
        if key_el == 0:
            break
        else:
            res.append(el)
            key_el -= 1
    return sorted_d_words


print(
    topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    )
)
# for k, v in sorted_d_words:
#     if key_el == 0:
#         break
#     res.append(k)
#     key_el -= 1
# return res
