class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_p = 0
        for i in range(len(prices)):
            min_p = min(prices[i], min_p)
            max_p = max(max_p, prices[i]-min_p)
        return max_p
        
        
    