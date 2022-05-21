# implementation of Binary Search Tree

class Node():
	def __init__(self , data):
		self.data = data
		self.left = None
		self.right = None


#Construction of BST

arr = [100,52,4,3,7,10,34,23,56]

root = Node(6)

def insertion(root , val):
	if root.left == None and val < root.data:
		newNode = Node(val)
		root.left = newNode
	elif root.right == None and val > root.data:
		newNode = Node(val)
		root.right = newNode
	else:
		if val < root.data:
			insertion(root.left , val)
		else:
			insertion(root.right , val)



for el in arr:
	insertion(root , el)

def find(root , el):
	if root == None:
		print(f"{el} is not present")
		return

	if 	root.data == el:
		print(f"{el} is present")
		return
	elif el > root.data:
		find(root.right , el)
	else:
		find(root.left , el)
	return


# find(root , 35)


# Lets Visualize Binary Search Tree

def printAll(root):
	if not root:
		return 
	print(root.data , end = " ")
	printAll(root.left)
	print()
	printAll(root.right)
	

printAll(root)