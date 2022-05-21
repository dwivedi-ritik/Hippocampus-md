
from more_itertools import pairwise

patt = "#$$#"

# Mid should be equal to $ and left should be # and right $

def solve(arr):
    for i , _ in enumerate(arr):
        if patt[i] == "$":
            l = i + 1
            r = i + 1

            while i >= int((l+r)/2):
                if arr[l] == "#" and arr[r] == "$":
                    l -= 1
                    r += 1
            res = arr[l:r+1] 
    print(res)


arr = [1 ,2 ,6 ,4 ,6]

for i , _  in enumerate(arr):
    if all( [  abs(x[0] - x[1]) <= 2 for x  in  pairwise(arr[:i] + arr[i+1:]) ]):
        print(True)
