# arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]

arr = [4, 2, 0, 3, 2, 5]
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# arr = [3, 1, 2, 4, 0, 1, 3, 2]


def naive(arr):
    n = len(arr)
    amount = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] >= arr[j]:
                temp = (j - i) * (arr[j])
            else:
                temp = (j - i) * (arr[i])
            if temp > amount:
                amount = temp
    return amount


def trapwater():
    left = []
    right = [0] * len(arr)
    h = -1
    for el in arr:
        if el > h:
            left.append(el)
            h = el
        else:
            left.append(h)
    h = -1
    j = len(arr) - 1
    for el in reversed(arr):
        if el > h:
            right[j] = el
            h = el
        else:
            right[j] = h
        j -= 1
    sum = 0
    i = 0
    for el in arr:
        sum = sum + min(left[i], right[i]) - el
        i += 1
    print(sum)
