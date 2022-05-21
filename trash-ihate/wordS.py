class Node:
    def __init__(self , c):
        self.c = c
        self.nodes = [None]*26
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = Node('\0')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            pos = ord(c) - 97
            if curr.nodes[pos] is None:
                curr.nodes[pos] = Node(c)
                curr = curr.nodes[pos]
            else:
                curr = curr.nodes[pos]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        res = []
        def rec(curr , word):
            if curr is None:
                return 

            for i , c in enumerate(word):
                if c == ".":
                    for node in curr.nodes:
                        if rec(node , word[i+1:]):
                            return True
                    return False
                else:
                    pos = ord(c) - 97
                    if curr.nodes[pos] is None:
                        return False
                    curr = curr.nodes[pos]
            return curr.endOfWord

        return rec(curr , word)
        






if __name__ == "__main__":
    t = Trie()
    t.insert("bad")
    t.insert("dad")
    t.insert("mad")
    print(t.search("pad"))
    print(t.search("bad"))
    print(t.search(".ad"))
    print(t.search("ba."))
    print(t.search("..."))
    
    # t.insert("b..")
    # print(t.search("..ad"))

# from typing import List
# def calPoints(ops: List[str]) -> int:
#     temp_stack = []
#     for c in ops:
#         if c == "C":
#             temp_stack.pop()
#         elif c == "D":
#             temp_stack.append( int(temp_stack[-1]) *2)
#         elif c == "+":
#             temp_stack.append(int(temp_stack[-1]) + int(temp_stack[-2]) )
#         else:
#             temp_stack.append(int(c))
            
#     return sum(temp_stack)

# print(calPoints(["5","-2","4","C","D","9","+","+"]))