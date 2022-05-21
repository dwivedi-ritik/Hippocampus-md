#N meeting in room

start  = [175250 ,50074, 43659 ,8931 ,11273 ,27545 ,50879 ,77924]
end = [112960 ,114515, 81825, 93424 ,54316, 35533, 73383 ,160252]

arr = [list(arr) for arr in zip(start , end)]
arr = sorted(arr , key=lambda x:x[-1])

last_m = arr[0][0]-1
total_m = 0
for s , e in arr:
    if last_m < s:
        total_m += 1
        last_m = e
# return total_m
print(total_m)