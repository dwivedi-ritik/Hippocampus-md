
# implementation of Trie data structer

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
        for c in word:
            pos = ord(c) - 97
            if curr.nodes[pos] is None:
                return False
            curr = curr.nodes[pos]
        return curr.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            pos = ord(c) - 97
            if curr.nodes[pos] is None:
                return False
            curr = curr.nodes[pos]
        return True