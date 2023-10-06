class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.value = 0



class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}

    def insert(self, word: str, val: int) -> None:
        diff = val - self.dic.get(word, 0)

        self.dic[word] = val
        
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                curr.children[ord(i) - ord('a')] = TrieNode()
            curr = curr.children[ord(i) - ord('a')]
            curr.value += diff
        

    def sum(self, word: str) -> int:
        curr = self.root
        for i in word:
            if not curr.children[ord(i) - ord('a')]:
                return 0
            curr = curr.children[ord(i) - ord('a')]
        return curr.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)