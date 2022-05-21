import math
from pprint import pprint

def get_dis(point1 , point2):
	val = abs(point2[0]- point1[0]) + abs(point2[1] - point1[1])
	return val

arr = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# arr = [[3,12],[-2,5],[-4,1]]

# arr.sort()

n = len(arr)
path = []
sum_ = 0
connected = []
for i in range(n):
	temp = []
	for j in range(n):
		if i != j:
			val = get_dis(arr[i] , arr[j])
			temp.append( (j , val) )
	path.append( { i:temp })


	
pprint(path)