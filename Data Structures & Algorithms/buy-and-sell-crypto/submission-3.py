class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        mx = 0
        for price in prices:

            lowest = min(lowest, price)
            mx = max(mx, price - lowest)
        return mx