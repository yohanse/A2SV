class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        answer = 0
        value, flag = prices[0], False
        for price in prices[1:]:
            if flag:
                if price > value:
                    answer += price - value
                    value = price
                else:
                    if price + fee < value:
                        value = price
                        flag = False
            else:
                if price - fee > value:
                    answer += price - fee - value
                    value = price
                    flag = True
                else:
                    value = min(value, price)
        return answer