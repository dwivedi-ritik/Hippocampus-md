# t = int(input())

def partition(arr):
    pivot = arr[-1]
    i = 0
    for j , el in enumerate(arr):
        if el < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[j] = temp
            i += 1
    
    temp = arr[j]
    arr[j] = arr[i]
    arr[j] = temp
    
    print(arr)
    return i

arr = [9,2,1,6,7,3]

print(partition(arr))

# for _ in range(t):
#     string = input()
#     mid = int(len(string)/2)
#     a = "".join( reversed(string[:mid]) )
#     b = "".join( reversed(string[mid:]) )
#     print(a+b)