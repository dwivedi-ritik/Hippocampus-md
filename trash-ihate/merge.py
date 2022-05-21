arr = [[1,3],[2,6],[8,10],[15,18]]

arr.sort()

temp = []
i = 0 


while i < len(arr)-1:
    if arr[i][-1] > arr[i+1][0]:
        el = arr[i][0]
        while arr[i][-1] > arr[i+1][-1]:
            i += 1
        temp.append([ el , arr[i][-1] ])
    else:
        temp.append(arr[i])

    i += 1
print(temp)