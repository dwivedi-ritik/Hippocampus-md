# Inorder traversal using iterative method
# What actually happen in recursion 
# We can simulate recursion using stack
# but the problem will be keeping track of value 
# in each recursive process 


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack , res = [] , []
    while True:
        
        while root is not None:
            stack.append(root)
            root = root.left
            
        if len(stack) == 0:
            break
        
        root = stack.pop()
        res.append(root.val)
        root = root.right
        
    return res