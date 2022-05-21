
def specialSum(m): 
    # Complete the function
    max_sum = 0
    i , j = 0 , 1
    while j < len(m)-1:
        if m[j] < m[j-1] and m[j] < m[j+1]:
            m[i] = m[j]-1
        
        else:
            max_sum += m[i]
            i += 1
            j += 1
        
    return max_sum + m[-1] + m[-2]
            

# print(specialSum([1,5,3,5,4]))

n = input()

n.isdigit()