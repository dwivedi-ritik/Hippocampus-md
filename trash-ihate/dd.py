try:
    t = input()
    for _ in range(int(t)):
        n = int(input())
        arr = [int(el) for el in input().split()]
        op = 0
        
        for el in arr:
            if (abs(el) & 1):
                op += 0
            else:
                op += 1
        if op & 1:
            print("NO")
        else:
            print("YES")
except Exception:
    pass

#LOSTSEQ