class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        N = len(word)
        curr = self.root

        def backTrack(index, curr):
            if index == N:
                return curr.is_end

            if word[index] != ".":
                return curr.children[ord(word[index]) - ord('a')] and backTrack(index + 1, curr.children[ord(word[index]) - ord('a')])
            
            
            for adj in curr.children:
                if adj and backTrack(index + 1, adj):
                    return True

            return False
        
        return backTrack(0, curr)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)