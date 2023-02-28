class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def rec(l, r, player_one, player_two, turn):
            if l > r:
                return player_one >= player_two

            if turn:
                return rec(l + 1, r, player_one + nums[l], player_two, False) or rec(l, r - 1, player_one + nums[r], player_two, False)
            return rec(l + 1, r, player_one, player_two + nums[l], True) and rec(l, r - 1, player_one, player_two + nums[r], True)
        return rec(0, len(nums) - 1, 0, 0, True)