class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, index):
        curr = self.root
        curr.val.add(index)
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
            curr.val.add(index)
            
    def search(self, word):
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                return set()
            curr = curr.children[ord(i) - ord('a')]
        return curr.val
            
class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.val = set()

class WordFilter:

    def __init__(self, words: List[str]):
        self.forward = Trie()
        self.backward = Trie()
        self.N = len(words)

        for i, word in enumerate(words):
            self.forward.insert(word, i)
            self.backward.insert(word[::-1], i)
        

    def f(self, pref: str, suff: str) -> int:
        ans1, ans2 = self.forward.search(pref), self.backward.search(suff[::-1])
        for i in range(self.N - 1, -1, -1):
            if i in ans1 and i in ans2:
                return i
        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)