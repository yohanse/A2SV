class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.is_end = True

    def insert(self, word):
        
        if not self.searchFull(word[:-1]):
            return False

        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
        curr.is_end = True
        return True
    
    def searchFull(self, word):
        word = word.lower()
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                return False
            curr = curr.children[ord(i) - ord('a')]
        return curr.is_end

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        dictionary = Trie()

        words.sort()
        ans = ""
        for word in words:
            if dictionary.insert(word) and len(word) > len(ans):
                ans = word
        return ans