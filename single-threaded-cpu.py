class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        for i in range(N):
            tasks[i] = [tasks[i][0], tasks[i][1], i]
        tasks.sort()
        num, ans = [], []
        start = time = 0

        while start < N:
            if num == [] and time < tasks[start][0]:
                time = tasks[start][0]

            while start < N and tasks[start][0] <= time:
                heappush(num, (tasks[start][1], tasks[start][2]))
                start += 1

            process, index = heappop(num)
            time += process
            ans.append(index)

        while num:
            process, index = heappop(num)
            ans.append(index)

        return ans