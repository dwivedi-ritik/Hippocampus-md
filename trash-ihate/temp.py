# def fib(i):
#     arr = []
#     arr.append(1)
#     arr.append(1)
#     for i in range(2 , i+1):
#         arr.append(arr[i-1]+ arr[i-2])
#     return arr[-2]


# def fib2(i , obj):
#     if i in obj:
#         obj[i]
#     if i == 1 or i == 2:
#         return 1
#     else:
#         obj[i] = fib2(i-1, obj) + fib2(i-2, obj)
#         return obj[i]

# print(fib(8))

# print(fib2(8 , {}))

# t = int(input())

# length = 0

# last = -1
# for _ in range(t):
#     n = int(input())
#     arr = map(int , input().split())
#     for el in arr:
#         if last == -1:
#             last = el
#             length += 1
#         elif el >  last:
#             length += 1
#             last = el
# print(length)


n = 4

# Permutation logic will be like iterate  each char and expect one

arr = []


def permutate(string, asf):
    if len(string) == 0:
        arr.append(asf)
        return

    for i, ch in enumerate(string):
        left_ss = string[:i]
        right_ss = string[i + 1 :]
        permutate(left_ss + right_ss, asf + string[i])


arr = [-1, 0, 1, 2, -1, -4]

sor
# permutate("dog", "")

# print(arr)
