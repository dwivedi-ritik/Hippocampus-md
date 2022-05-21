from collections import Counter

s1 = "aboooo"

s2 = "eidbaooo"


# def check(s1, s2):
#     s1_dict = Counter(s1)
#     s2_dict = Counter(s2)

#     for k in s1_dict:
#         if s1_dict[k] != s2_dict[k] and s1_dict[k] > s2_dict[k]:
#             return False

#     return True


# print(check(s1, s2))
# from collections import Counter


# s = input()

# p = input()


def check(s_dict, p_dict):
    for k in p_dict:
        if s_dict[k] != p_dict[k]:
            return False
    return True


def anna_list(s, p):
    p_dict = Counter(p)
    p_len = len(p)
    s_dict = Counter(s[0 : p_len - 1])
    s_len = len(s)

    i = 0

    j = p_len - 1

    res = []

    while j < s_len:

        if s[j] not in s_dict:
            s_dict[s[j]] = 1
        else:
            s_dict[s[j]] += 1

        if check(s_dict, p_dict):
            res.append(i)

        if s_dict[s[i]] == 1:
            s_dict.pop(s[i], None)
        else:
            s_dict[s[i]] -= 1

        i += 1
        j += 1

    return res


print(anna_list(s, p))

# print(")
