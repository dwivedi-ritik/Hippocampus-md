from typing import List

#Weird Ass
def nextPermutation(nums: List[int]) -> None:
    length = len(nums)
    pv = 0
    for i in range(length-1 , 0 , -1):
        if nums[i-1] < nums[i]:
            pv = i
            break

    if pv == 0:
        nums = nums[::-1]
        print(nums)
        return
    
    i = length - 1
    
    while nums[pv - 1] >= nums[i]:
        i -= 1
        
    nums[pv - 1] , nums[i] = nums[i] , nums[pv-1 ]
    nums[pv:] = sorted(nums[pv:])

# nextPermutation([3,2,1])

# Pascal Triangle
def generate(numRows: int) -> List[List[int]]:
    print(numRows)

    res = [[1],[1,1],[1,2,1]]
    if len(res) < 4:
        return res[:numRows]
    
    print(numRows)

    numRows -= 3
    while numRows != 0:
        temp = []
        temp.append(1)
        for i in range(len(res[-1]) - 1):
            temp.append(res[-1][i]+res[-1][i+1])
        numRows -= 1
        temp.append(1)
        res.append(temp)
        print(temp)
    return res

# print(generate(5))

#Count number of subarray with 0 sum
def maxLen(arr):
    #Idea is to find the consecutive sum 
    #If that sum repeats this means sum is 0
    obj = {}
    sum_  = 0 
    max_len = 0
    
    for pos , el in enumerate(arr):
        sum_ += el
        
        if sum_ == 0 and max_len < pos+1:
            max_len = pos+1

        if sum_ in obj:
            curr_len = pos - obj[sum_]
            if curr_len > max_len:
                max_len = curr_len
        else:
            obj[sum_] = pos
    return max_len

# arr1 = [15,-2,2,-8,1,7,10,23]
# arr2 = [-1 , 1 , -1 , 1]
# print(maxLen(arr2))

# Subarray with given XOR
## Very Very Asshole type of question
def solve(self, A, B):
    sum_ = 0
    ans = 0
    obj = {}
    for el in A:
        sum_ = sum_ ^ el
        if sum_ == B:
            ans += 1
        
        if sum_ ^ B in obj:
            ans += obj[sum_ ^ B]
        
        if sum_  in obj:
            obj[sum_] += 1
        else:
            obj[sum_] = 1

    return ans

print(solve([5,6,7,8,9] , 5))
