class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=1
        mx = 0
        for l in range(len(prices)-1):
            r = prices.index(max(prices[l+1:]))
            dif = prices[r] - prices[l]
            if dif > mx:
                mx = dif
        return mx