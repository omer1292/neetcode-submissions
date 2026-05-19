class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0
        hm = {}
        for r in range(len(s)):
            if s[r] in hm and hm[s[r]] >= l:
                l = hm[s[r]] + 1

            hm[s[r]] = r
            mx = max(mx, r - l + 1)

        return mx