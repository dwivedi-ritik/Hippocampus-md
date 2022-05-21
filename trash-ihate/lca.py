
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # First node where they split

    def dfs(root , p , q) :
        if root is None:
            return None
        if root.val < p and root.val < q:
            return dfs(root.right , p , q)
        if root.val > p and root.val > q:
            return dfs(root.left , p , q)
        return root
            
        
    return dfs(root , p.val , q.val)


# string = "dsahjpjauf"

# seq_to_search = "ahjpjau"

# 1 - iterate each element of $(seq_to_search):
# 2 - pos = find positon of ith character of $(seq_to_search) that matches in string:
# 3 - Repeat 2nd step but
# 4 - instead of searching from 0th index of string 
# 5 - start from $(pos)  


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last_index = 0
        for c in s:
            new_index = self.index(t , c , last_index)
            if new_index == -1:
                return False
            last_index = new_index + 1
        
        return True
    
    def index(self , string , c , start):
        n = len(string)
        
        while start < n:
            if string[start] == c:
                return start
            start += 1
        
        return -1 
    
45 Leyton 3 = checkIn
32 Paradise 8 = checkIn
27 Leyton 10 = checkIn