from collections import Counter


def check(temp, t_dict):
    count = 0
    for t_key in t_dict:
        if t_key in temp and t_dict[t_key] <= temp[t_key]:
            count += 1
        else:
            return count
    return count


def minWindow():
    s = "cabwefgewcwaefgcf"
    t = "cae"
    max_str = ""
    t_dict = Counter(t)
    t_len = len(t_dict)

    i, j = 0, 0

    temp = {}

    while j < len(s):
        match_count = 0

        el = s[j]

        if el in temp:
            temp[el] += 1
        else:
            temp[el] = 1

        # check if current counter is in t_dict
        while check(temp, t_dict) == t_len:

            if temp[s[i]] > 1:
                temp[s[i]] -= 1
            else:
                temp.pop(s[i], None)
            if max_str == "":
                max_str = s[i : j + 1]
            elif len(max_str) > len(s[i : j + 1]):
                max_str = s[i : j + 1]

            i += 1

        j += 1
