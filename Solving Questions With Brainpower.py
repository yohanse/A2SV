class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        for i in range(N - 2, -1, -1):
            point, brain = questions[i]
            num = 0
            if i + brain + 1 < N:
                num = questions[i + brain + 1][0]
            questions[i][0] = max(questions[i][0] + num, questions[i + 1][0])

        return questions[0][0]