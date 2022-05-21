def equalize(arr , n):
    
    sum_arr = sum(arr)
    
    diff_sum = 0
    eq = sum_arr / n
    
    for i in range(0, n):
        diff_sum += abs(arr[i] - eq)
 
    return int(diff_sum / 2)    

i = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = [ int(x) for x in input().split()]

    pos = equalize(arr , n)
    print("Set #{}".format(i))
    print("The minimum number of moves is {}.\n".format(pos))
    i += 1
    
        
