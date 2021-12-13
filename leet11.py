# finding longest consigutive 1s


temp_str = "0111010011"


# better approch will be count consecutive 0s and 1s seperately
one_count = 0
zero_count = 0
count = 0
for el in temp_str:
    if el == "0":
        count = 0
    else:
        count += 1
        if count > one_count:
            one_count = count

count = 0
for el in temp_str:
    if el == "1":
        count = 0
    else:
        count += 1
        if count > zero_count:
            zero_count = count

print(one_count, zero_count)


# counting longest consecutive substring
def maxPower(s):
    max_count = 1
    if len(s) == 0:
        max_count = 0
    last_count = 0
    temp = {}
    for el in s:
        if el in temp:
            temp[el] += 1
            last_count = temp[el]
        else:
            temp = {}
            temp[el] = 1
            if last_count > max_count:
                max_count = last_count
            last_count = 0
    if last_count > max_count:
        max_count = last_count

    return max_count


print(maxPower("ahgsaaaabs"))
