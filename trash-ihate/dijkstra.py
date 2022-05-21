import heapq
from typing import List
from collections import defaultdict

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj_list = defaultdict(list)
    
    for s, d, t in times:
        adj_list[s].append((d,t))

    heap_source = [(0 , k)]
    
    visited = set()
    
    while heap_source:
        last_time , last_source  = heapq.heappop(heap_source)

        visited.add(last_source)
        
        if len(visited) == n:
            return last_time
        
        for adj , time in adj_list[last_source]:
            if adj not in visited:
                heapq.heappush(heap_source ,(time+last_time , adj))
    
    return -1
if __name__ == "__main__":
	print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]] , 4 , 2))