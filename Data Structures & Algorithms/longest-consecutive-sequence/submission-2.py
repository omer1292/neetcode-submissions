class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        listso = sorted(set(nums))
        mx = 1
        cur = 1
        for i in range(1, len(listso)):
            if listso[i] == listso[i-1] + 1:
                cur +=1
            else:
                cur = 1
            mx = max(mx,cur)

        return mx
        