class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff >0:
                result += diff
        return result