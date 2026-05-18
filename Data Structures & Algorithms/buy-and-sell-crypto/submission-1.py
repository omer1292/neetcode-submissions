class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        mx = 0
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            mx = max(mx, prices[i] - lowest)
        return mx