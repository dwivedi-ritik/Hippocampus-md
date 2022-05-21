#I have to make an algorithm that return the maximum product of given array

# arr = [-2,0,-1]
# # arr = [2,3,4 ,-3,4]

# dp = [0]*(len(arr))

# length = len(arr)
# s = 1
# for i in range(length):
#     s *= arr[i]
#     dp[i] = max(s , dp[i-1])
#     if s <= 0:
#         s = 1
# print(dp[-1])

#I have to find the minimum steps require to make t anagram of s

def minSteps( s: str, t: str) -> int:
    table1 = [0]*26
    table2 = [0]*26
    for s1 , t1 in zip(s , t):
        table1[ord(s1) - 97] += 1
        table2[ord(t1) - 97] += 1
    count = 0
    # Though we need to find the whether t can be an annagram of s so we 
    # we just have to check the difference count of t and s
    
    for i in range(len(table1)):
        if table2[i] > table1[i]:
            count += table2[i] - table1[i]

    return count 


    



print(minSteps("practice" , "leetcode"))