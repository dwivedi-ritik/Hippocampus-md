# from itertools import permutations
# count = 0
# n = int(input())
# arr = list(range(1 , n+1))

# for a in permutations(arr):
# 	for e in a:
# 		if a[e-1] == e:
# 			print(a)
# 			count += 1
# 			break

# print(count)

# decode ways

# 263
# total_ways = 0
s = "2323241212"
memo = {len(s): 1}

# def check(i):
# 	if i in memo:
# 		return memo[i]

# 	if s[i] == "0":
# 		return 0

# 	res = check(i+1)
# 	if (i+1 < len(s) and ( s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")) ):
# 		res += check(i+2)
	
# 	memo[i]= res
	
# 	return res

# if __name__ == "__main__":
# 	print(check(0)) 

# 2 is valid
# 22 is valid
# 226 is not
# 263

# def find_gcd(x, y):
     
#     while(y):
#         x, y = y, x % y
     
#     return x
         
# n = input()
# l = [int(n) for n in input().split()]

# num1 = l[0]
# num2 = l[1]
# gcd = find_gcd(num1, num2)
 
# for i in range(2, len(l)):
#     gcd = find_gcd(gcd, l[i])
     
# print(gcd)

def findLength(nums1, nums2):
    # LCS table
    max_match = 0
    r , c = len(nums1) , len(nums2)
    
    table =[[]]*(c+1)
    for i in range(r+1):
        
        for j in range(c+1):
            if (j == 0):
                table[j].append(0)
            elif(nums1[i-1] == nums2[j-1]):
                table[j].append(1 + table[i-1][j-1])
    print(table)

findLength([1,2,3,2,1] , [3,2,1,4,7])