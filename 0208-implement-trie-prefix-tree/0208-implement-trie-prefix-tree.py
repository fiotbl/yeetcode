class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            index = ord(w) - ord("a")
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True
                

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            index = ord(w) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            index = ord(w) - ord("a")
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)