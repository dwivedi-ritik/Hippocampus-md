import more_itertools

arr = [2, 3, 1, 2, 4, 3]
target = 7


i, j = 0, 0

count = 0
sum_val = 0
temp = []
min_el = 0
while j < len(arr):
    sum_val += arr[j]

    while sum_val >= target:
        if min_el == 0:
            min_el = j - i + 1
        elif min_el > (j - i + 1):
            min_el = j - i + 1
        sum_val -= arr[i]
        i += 1

    j += 1

print(min_el)
