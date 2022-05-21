# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/submissions/
# stack = []
                    
# for el in s:
#     if stack and stack[-1][0] == el:
#         stack.append( (el , stack[-1][1]+1) )
#     else:
#         stack.append( [el , 1] )
    
#     if stack and len(stack) >= k:
    
#         if stack[-1][1] == k:
#             for _ in range(k):
#                 stack.pop()    

# return "".join([el[0] for el in stack ])

#  Question is based on monotonic stack and pair
def solve(nums):
    if len(nums) < 3:
        return False

    i , j , k = 0 , 1 , 2

    while k < len(nums):
        if nums[i] < nums[k] > nums[j]:
            return True
        i += 1
        j += 1
        k += 1
    return False

print(solve([3,5,0]))