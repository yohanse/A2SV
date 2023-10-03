class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
        curr.is_end = True
    
    def searchFull(self, word):
        word = word.lower()
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                return False
            curr = curr.children[ord(i) - ord('a')]
        return curr.is_end

    def searchPrefix(self, word):
        word = word.lower()
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                return False
            curr = curr.children[ord(i) - ord('a')]
        return True
            



class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]


