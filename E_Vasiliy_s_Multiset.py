class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, binary):
        curr = self.root
        for i in binary:
            if i == "0":
                if not curr.zero:
                    curr.zero = TrieNode()
                curr = curr.zero
            else:
                if not curr.one:
                    curr.one = TrieNode()
                curr = curr.one
            curr.val += 1
            
    def delete(self, binary):
        curr = self.root
        for i in binary:
            if i == "0":
                curr = curr.zero
            else:
                curr = curr.one
            curr.val -= 1
    
    def search(self, binary):
        curr = self.root
        power = 2 ** 31
        ans = 0
        for i in binary:
            if i == "0":
                if curr.one and curr.one.val > 0:
                    ans += power
                    curr = curr.one
                elif curr.zero and curr.zero.val > 0:
                    curr = curr.zero
                else:
                    return ans
            else:
                if curr.zero and curr.zero.val > 0:
                    ans += power
                    curr = curr.zero
                elif curr.one and curr.one.val > 0:
                    curr = curr.one
                else:
                    return ans
            power //= 2
        return ans

class TrieNode:
    def __init__(self):
        self.val = 0
        self.zero = None
        self.one = None


trie = Trie()
q = int(input())
binary = "0" * 32
trie.insert(binary)
for i in range(q):
    operation, num = list(input().split())
    binary = bin(int(num))[2:]
    binary = "0" * (32 - len(binary)) + binary
    if operation == "+":
        trie.insert(binary)

    elif operation == "-":
        trie.delete(binary)

    else:
        print(trie.search(binary))

