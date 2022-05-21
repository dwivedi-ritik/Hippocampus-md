arr1 = "abcd100[leetcode]"
arr1 = "3[a]2[bc]"
        

arr2 = list(arr1)

last_len = 0

for i , el in enumerate(arr1):
    if el == "]":
        j = i + last_len - 1
        substr = ""
        while ( arr2[j] != "["):
            substr += arr2[j]
            j -= 1
        j -= 1
        num = ''
        while arr2[j].isdigit():
            num += arr2[j]
            j -= 1
        # j -= 1
        temp_str = int(num[::-1])*"".join(reversed(substr))
        
        arr2[j:i+last_len+1] = temp_str
        
        last_len = len(temp_str) + len(num)- (i - j + 1)

print("".join(arr2))


