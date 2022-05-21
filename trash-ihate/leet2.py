#Finding the length of largest substring
def main():
    x = "abcabcbb"
    temp = 0
    max = 0
    length = len(x)
    temp_d = {}
    for i in range(length):
        for j in range(i , length):
            if x[j] in temp_d:
                break
            else:
                temp_d[ x[j] ] = 1
        temp = len(temp_d)
        temp_d = {}
        if temp > max:
            max = temp
        temp = 0
    print(max)


if __name__ == "__main__":
    main()
