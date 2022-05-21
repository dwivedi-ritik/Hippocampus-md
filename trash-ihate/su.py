# n = input()

# all_4_digit = ['8008', '1001', '9006', '6009', '8888', '1881', '9886', '6889', '8118', '1111', '9116', '6119', '8968', '1961', '9966', '6969', '8698', '1691', '9696', '6699']

# res  = []

# count = 0
# for el in all_4_digit:
# 	count  = 0
# 	for el2 in el:
# 		if el2 in n:
# 			count += 1
# 	if count == 4:
# 		res.append(el)


# print(",".join(res))

# t = input()
# for _ in range(int(t)):
#     n = input()
#     r , p = 0 , 1
#     arr = [int(n) for n in input().split()]
#     for i in range(int(n)):
#         if arr[i] == i+p:
#             r += 1
#             p += 1
#     print(r)

# t = input()
# for _ in range(int(t)):
#     n = int(input())

#     b_arr = list(input())

#     ones , zeros = 0 , 0 
#     for el in b_arr:
#         if el == '0':
#             zeros += 1
#         else:
#             ones += 1
#     print(b_arr)    
#     if n%2 == 0:
#         if ones == zeros:
#             print("YES")
#         elif ones%2 == 0 and zeros%2 == 0:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("YES")

# t = input()
# for _ in range(int(t)):
#     n = int(input())
#     arr = [int(el) for el in input().split()]
#     for i in range(n):
#         for j in range(i+1 , n):
#             if arr[i]&arr[j] != 0:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     t = arr[0]
#     flag = 0
#     for el in arr:
#         if el > t:
#             flag = 1
#             print("No")
#             break
#     if flag == 0:
#         print("Yes")

arr = [9 ,34 ,4 ,24 ,1 ,6]

temp = []

sum_ = 0
for el in arr:
	sum_ = sum_ ^ el
	temp.append(sum_)

print(temp)