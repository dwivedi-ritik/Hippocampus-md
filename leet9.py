arr = ["eat", "tea", "tan", "ate", "nat", "bat"]


def is_anna(str1, str2):
    chars = [0] * 26
    if len(str1) != len(str2):
        return False
    for s1, s2 in zip(str1, str2):
        is1 = ord(s1)
        is2 = ord(s2)
        chars[97 - is1] = chars[97 - is1] + 1
        chars[97 - is2] = chars[97 - is2] - 1
    for el in chars:
        if el != 0:
            return False
    return True


res = []
anna_group = {}
for el in arr:
    sorted_el = "".join(sorted(el))
    if anna_group.get(sorted_el) == None:
        anna_group[sorted_el] = []
        anna_group[sorted_el].append(el)

    else:
        anna_group[sorted_el].append(el)

res = [grp_arr for grp_arr in anna_group.values()]

print(res)
