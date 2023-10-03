class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
            curr.val += 1
    
    def search(self, word):
        curr = self.root
        ans = 0
        for i in word:
            curr = curr.children[ord(i) - ord('a')]
            ans += curr.val
        return ans

class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = [None for i in range(26)]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = [0 for i in range(len(words))]
        for i, word in enumerate(words):
            ans[i] = trie.search(word)  
        return ans      