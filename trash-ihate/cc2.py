def check_ith_bit(n, i):
    if (n & (1 << (i - 1))):
        return True
    else:
        return False
 
def no_of_flips(n , length):
    ln = length
    ans = 0
    right = 1
    left = ln
    while (right < left):
        if (check_ith_bit(n, right) !=
            check_ith_bit(n, left)):
            ans += 1
        left -= 1
        right += 1
    return ans


def check(string , k):
    i = 0
    c = 0
    j = len(string) - 1

    while i < j :
        if string[i] != string[j]:
            c += 1
        i += 1
        j -=1

        if c > k:
            return False

    left = len(string) - c
    
    if c == k or c + left == k:
        return True
    return False



# print(check("110" , 0)) 

# try:
t = input()
for _ in range(int(t)):
    _ , c = map(int , input().split())
    string = input()
    
    if check(string , c):
        print("YES")
    else:
        print("NO")
    
# except Exception:
#     pass