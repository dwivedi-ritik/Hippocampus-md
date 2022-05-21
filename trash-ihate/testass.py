def combinationSum(candidate , target):
	ans = []
	def dfs(i , curr_sum , curr_list):
		if curr_sum == target:
			print(curr_list)
			ans.append(curr_list)
		if curr_sum > target or i > len(candidate):
			return

		for j in range(i , len(candidate)):
			curr_list.append(candidate[j])
			dfs(j , curr_sum + candidate[j] , curr_list)
			curr_list.pop()
	dfs(0,0, [])
	return ans



# nums = [-2,1,-3,4,-1,2,1,-5,4]

# s = 0

# s = sum(nums)


# for el in nums:
# 	if s - el > s:
# 		s = s - el

# print(s)

# n , b , c = 105 , 80 , 10

# m_b = b
# m_c = c
# bus_cost = []
# car_cost = []
# for i in range(1 , n+1):
# 	if i % 100 == 0:
# 		b += m_b
# 	bus_cost.append(b)


# for i in range(1 , n+1):
# 	if i % 4 == 0:
# 		car_cost.append(c)
# 		c += m_c
# 	else:
# 		car_cost.append(c)

# print(bus_cost)
# print(car_cost)



# arr = ")()()((()"

# for el in arr:
# 	arr.pop()
# 	

try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        bin_str = input()
        temp_arr = {}
        res , count = 0 , 0
        for i in range(n):
            temp = bin_str[:i]+bin_str[i+1:]
            if temp_arr.get(temp) is None:
                temp_arr[temp] = 1
                count += 1
            res = max(res , count)
        print(res)
except Exception:
    pass