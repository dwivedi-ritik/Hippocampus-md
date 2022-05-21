from string import ascii_lowercase

words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]

score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

temp = {i: j for i, j in zip(ascii_lowercase, score)}

num_arr = []
flag = 0
for word in words:
    word_sum = 0
    flag = 0
    for char in word:
        if char not in letters:
            flag = 1
            break
        word_sum += temp[char]
    if not flag:
        num_arr.append(word_sum)
print(num_arr)
