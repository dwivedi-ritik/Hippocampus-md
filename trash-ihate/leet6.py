from collections import Counter

#Naive Approach
def main(nums):
    range_arr = list(range(1 , len(nums)+1))
    count_nums = Counter(nums)
    res_arr = []
    for i in range_arr:
        if not count_nums.get(i):
            res_arr.append(i)

    return res_arr


if __name__ == "__main__":
    main([4, 3, 2, 7, 8, 2, 3, 1])