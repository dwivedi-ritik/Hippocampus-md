from typing import List

# Hash Bucket

class MyHashSet:

    def __init__(self):
        self.size = 2003
        self.data = [[] for _ in range(self.size)] 

    def add(self, key: int) -> None:
        pos = key%self.size
        self.data[pos].append(key)

    def remove(self, key: int) -> None:
        pos = key%self.size
        if key in self.data[pos]:
            self.data[pos].remove(key)
            
    def contains(self, key: int) -> bool:
        pos = key%self.size
        if key in self.data[pos]: return True
        return False


# Binary tree from inorder and postorder

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder_: List[int]):
    
    
    def construct(inorder):
        if not inorder: return None
        
        root = TreeNode()
        
        # print(inorder)
        for p in preorder:
            if p in inorder:
                root.val = p
                break
        preorder.pop(0)
        
        i = inorder.index(root.val)
        root.left = construct(inorder[:i])
        root.right = construct(inorder[i+1:])
        return root

        
    root = construct(inorder_)
    
    return root


if __name__ == "__main__":
    h = MyHashSet()
    h.add(1)
    h.add(2)
    print(h.contains(2))
    r = buildTree([3,9,20,15,7] , [9,3,15,20,7])


# if not inorder: return
            
#             root = TreeNode()
            
#             prev = root
            
            
#             root.val = preorder.pop(0)
            
            
#             i = inorder.index(root.val)
            
#             left_subarr = inorder[:i]
#             right_subarr = inorder[i+1:]
            
#             left , right = None , None
            
#             for p in preorder:
#                 if p in left_subarr:
#                     left = p
#                     break;
#             root.left = p
            
#             for p in preorder:
#                 if p in right_subarr:
#                     left = p
#                     break;
#             root.right = p
            
#             construct(root.left , inorder)
#             construct(root.right , inorder)
#         


