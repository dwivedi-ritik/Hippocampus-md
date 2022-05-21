# Product of array except self

# Get left subarray and get right subarray

def check(arr):
	last_val = 1
	left_sum = [0]*len(arr)
	right_sum = [0]*len(arr)

	for i , _ in enumerate(arr):
		left_sum[i] = arr[i]*last_val
		last_val = arr[i]*last_val
	
	last_val = 1
	for i in range(len(arr)-1 , -1 , -1):
		right_sum[i] = arr[i]*last_val
		last_val = arr[i]*last_val

	res = []
	for i in range(len(arr)):
		if i == 0:
			res.append(right_sum[i+1])
		elif i == (len(arr) - 1): 
			res.append(left_sum[i-1])
		else:
			res.append(left_sum[i-1]*right_sum[i+1])

	return res
if __name__ == "__main__":
	print(check([1,2,3,4 ]))
	print(check([-1,1,0,-3,3]))
        