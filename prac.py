# vowel substring


def vowel(string):
    vowels = "aeiou"
    res = []
    temp_str = ""
    res_str = ""
    for el in string:
        if el in vowels:
            temp_str += el
        else:
            res_str = max(temp_str, res_str)
    res_str = max(temp_str, res_str)

    return len()

    # count = 0
    # max_count = 0
    # for el in string:
    #     if el in vowels:
    #         count += 1
    #     else:
    #         count = 0
    #     if count > max_count:
    #         max_count = count

    # return max_count


print(vowel("cuaieuouac"))
