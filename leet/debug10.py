from collections import Counter


def frequencySort(s):
    s_dict = Counter(s)
    res = ""
    sorted_s_dict = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_s_dict:
        res += k * v
    return res


def topKFrequent(self, nums: List[int], key: int) -> List[int]:
    d_nums = Counter(nums)
    res = []
    sorted_d_nums = sorted(d_nums.items(), key=lambda x: x[1], reverse=True)

    for k, v in sorted_d_nums:
        if key == 0:
            break
        res.append(k)
        key -= 1
    return res


# print(topFreq([1, 1, 1, 2, 2, 3], 2))
# print(frequencySort("Treeaaaaabbccdeg11111113344"))
