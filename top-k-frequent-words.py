class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict()
        for i in words:
            dic[i] = dic.get(i, 0) + 1

        num = []
        for i in dic:
            num.append((-dic[i], i))
        
        heapify(num)
        ans = []
        for i in range(k):
            ans.append((heappop(num)[1]))

        return ans