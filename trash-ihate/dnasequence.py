from collections import Counter

def dnasequence(s):	
	i = 0 
	j = 10
	d_arr = []
	
	while j <= len(s):
		temp = s[i:j]
		d_arr.append(temp)
		i += 1
		j += 1
	
	d_arr_count = Counter(d_arr)
	
	res = [k for k , v in d_arr_count.items() if v > 1]
	return res

def insertintervals(intervals , newintervals):
	#Combining all intervals
	arr = []
	for interval in intervals:
		for el in interval:
			arr.append(el)

	i , res = 0 , []

	while i < len(arr):
		if arr[i] > arr[0]:
			break
		else:
			res.append(arr[i])
		i += 1
	
	inter_1 = i
	
	while i < len(arr):
		if arr[1] > arr[i]:
			break

	while i < len(arr):
		res.append(arr[i])

	res_res = []
	for j in range(0 , len(arr) , 2):
		temp = [arr[j] , arr[j+1]]
		res_res.append(temp)

	return res_res
