# Code Vita 1

# Civil War

n = int(input())

arr = [int(el) for el in input().split()]

checker = 0
i , j = 0 , len(arr) - 1
k1 , k2 = i , j
cap , iron = 0 , 0 


while i < n-1 and j >= 0:
    if arr[i] is not None and (cap+arr[i]) > cap:
        cap += arr[i]
        arr[i] = None
        i += 1
        k1 += 1
    else:
        i += 1
  
    if arr[j] is not None and (iron+arr[j]) > iron:
        iron += arr[j]
        arr[j] = None
        j -= 1
        k2 -= 1
    else:
        j -= 1



while k2 >= 0:
    if arr[k2] is not None:
        iron += arr[k2]
    k2 -= 1
while k1 < n:
    if arr[k1] is not None:
        cap += arr[k1]
    k1 += 1

print(cap , iron)
print(abs(cap-iron))