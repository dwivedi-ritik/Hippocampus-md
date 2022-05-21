# I just have to find the pivot element postion in array
# Where


def gettingPivot(arr, l, h):
    if l <= h:
        m = int((l + h) / 2)
        try:
            if arr[m] > arr[m + 1]:
                return m
            elif arr[l] <= arr[m]:
                return gettingPivot(arr, m + 1, h)
            else:
                return gettingPivot(arr, l, m - 1)
        except Exception:
            return m


def bsearch(arr, l, r, key):
    if l <= r:
        m = int((l + r) / 2)
        if arr[m] == key:
            return m
        elif arr[m] < key:
            return bsearch(arr, m + 1, r, key)
        else:
            return bsearch(arr, l, m - 1, key)

    return -1


nums = [1, 0, 1, 1, 1]


def search(nums, key):
    pi = gettingPivot(nums, 0, len(nums) - 1)
    print(pi)
    if key > nums[0]:
        pos = bsearch(nums, 0, pi, key)
    else:
        pos = bsearch(nums, pi + 1, len(nums) - 1, key)

    print(pos)


search(nums, 0)
