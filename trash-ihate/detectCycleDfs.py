from typing import List
from collections import defaultdict
# edges = [[1,0] , [1,0]]
# 5
edges = [[1,4],[2,4],[3,1],[3,2]]

# for i , edge in enumerate(edges):
# 	print(f"{i}-{edge}")

# def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
#     visited = [False for _ in range(numCourses) ]
    
#     def dfs(i , p):
        
#         if not visited[i]:
#             visited[i] = True

#             for el in prerequisites[i]:
#                 if visited[el] and el != p:
#                     return False
#                 else:
#                     visited[el] = True
#                 dfs(el , i)
#         return True
                
#     return dfs(0 , 0)

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = defaultdict(list)

    visited = [ False for _ in range(numCourses) ]
    for c , p in prerequisites:
        adj_list[c].append(p) 
    print(adj_list)

    def has_cycle(i , p):
        if p != -1 and visited[p] and visited[i]:
            return True
        else:
            visited[i] = True

            for el in adj_list[i]:
            	has_cycle(el , i)

    for c , p in prerequisites:
        if has_cycle(c , c):
            return False
    return True
if __name__ == "__main__":
	print( canFinish(5 , edges) )