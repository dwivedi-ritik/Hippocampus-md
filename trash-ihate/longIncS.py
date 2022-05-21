# Longest increasing subsequence

arr = [0,1,0,3,2,3]

dp = [1]*len(arr)

length = len(arr)

for i in range(length):
    j = i-1
    while j >= 0:
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + 1:
               dp[i] = dp[j]+1  
        j -= 1
    
print(dp[-1])
