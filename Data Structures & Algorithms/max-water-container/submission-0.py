class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        mx = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                s = min(heights[i], heights[j])
                if s*(j-i) > mx:
                    mx = s*(j-i)
        return mx
        