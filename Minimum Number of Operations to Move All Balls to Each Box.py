class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)                                              #assign variable
        to_run_to_right, to_run_to_left, ans = [0]*N, [0]*N, [0]*N

        number_of_one = int(boxes[0])
        for i in range(1,N):
            to_run_to_right[i] = to_run_to_right[i - 1] + number_of_one #to move 1's to right
            number_of_one += int(boxes[i])

        number_of_one = int(boxes[-1])
        for i in range(N - 2, -1, -1):
            to_run_to_left[i] = to_run_to_left[i + 1] + number_of_one # to move 1's to left
            number_of_one += int(boxes[i])

        for i in range(N):
            ans[i] = to_run_to_left[i] + to_run_to_right[i] 

        return ans