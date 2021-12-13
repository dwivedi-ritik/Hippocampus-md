string = ["2", "[", "ab", "]"]

i = 0

temp = ""

n = ""

brac = ""
flag = 0

for el in string:
    if el.isdigit():
        n += el
    elif flag == 1:
        brac += el
    elif el == "[":
        flag = 1
    elif el == "]":
        temp += int(n) * brac
        flag = 0
    else:
        temp += el

print(temp)
