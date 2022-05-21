def backspaceCompare(s , t):

	stack1 , stack2 = [] , []
	for el in s:
		if el == "#" and len(stack1):
			stack1.pop()
		else:
			if el != "#":
				stack1.append(el)
	for el2 in t:
		if el2 == "#" and len(stack2):
			stack2.pop()
		else:
			if el2 != "#":
				stack2.append(el2)
	print(stack2 , stack1)
	c1 , c2 = "".join(stack1) , "".join(stack2)
	if c1 == c2: return True
	return False

	


arr = [[0,6],[2,3],[2,6],[2,7],[1,7],[2,4],[3,5],[0,2]]
# arr = [[0,1],[0,2],[0,3],[1,2],[1,3]]
n = 8
parents = [ i for i in range(n+1) ]
ranks = [1]* (n+1)


def find(n):
    p = parents[n]
    while p != parents[p]:
        p = parents[p]
    return p

def union(n1 , n2):
    p1 , p2 = find(n1) , find(n2)

    if p1 == p2:
        return False

    if ranks[p1] > ranks[p2]:
        parents[p2] = p1
        ranks[p1] += 1
    else:
        parents[p1] = p2
        ranks[p2] += 1
        
    return True

loops = 0

for x , y in arr:
	if not union(x ,y):
		loops += 1
	else:
		n -= 1

if (n - 1) > loops:
	print(-1)
else:
	print(n-1)

# if __name__ == "__main__":
# 	print(backspaceCompare("ab##" , "c#d#"))
	# print(backspaceCompare("bxj##tw","bxo#j##tw"))
	# print(backspaceCompare("y#fo##f" , "y#f#o##f"))
# 	

