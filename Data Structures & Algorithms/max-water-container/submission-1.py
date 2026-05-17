class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        mx = 0

        while l<r:
            s = min(heights[l], heights[r])
            if s*(r-l) > mx:
                mx = s*(r-l)
            if heights[l] == min(heights[l], heights[r]):
                l+=1
            else:
                r-=1
            

        return mx
        