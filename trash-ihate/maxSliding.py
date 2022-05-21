#First let me try the brute force
#I have to find the max number in each window
#I can create a stack that will be representated as a each slide in the array
#But i have to find the max element in each stack


def maxSlidingWindow(arr , r):
	stack = []
	res = []
	stack = arr[:r]
	max_el = max(stack)
	i , up_bound  = r , len(arr)
	n = 0
	while i < up_bound:
		res.append(max_el)
		stack.pop(0)
		stack.append(arr[i])

		if arr[i] >= max_el and i%r != 0:
			max_el = arr[i]
		else:
			n += 1
			max_el = max(stack)
		
		i += 1
	res.append(max_el)
	print(n)
	return res	

# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7] , 3))

from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    g_stack = []
    map_obj = {}
    for el in nums2[::-1]:
    	if not len(g_stack):
    		g_stack.append(el)
    		map_obj[el] = -1
    	elif len(g_stack):
	    	while len(g_stack) and el > g_stack[-1]:
	    		g_stack.pop(-1)
    		if not len(g_stack):
    			g_stack.append(el)
    			map_obj[el] = -1
    		else:
    			map_obj[el] = g_stack[-1]
    	else:
    		pass
    	g_stack.append(el)

    return [map_obj[n] for n in nums1]

nextGreaterElement([4,1,2] , [1,3,4,2])
