from collections import Counter


def main(s , t):
    obj = {}
    for x , y in zip(s,t):
        if obj.get(x) and obj[x] != y:
            return False
        obj[x] = y
    return True

if __name__ == "__main__":
    print(main("fxy" , "bo"))