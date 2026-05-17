class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sor = sorted(nums)
        out = []
        for i in range(len(nums)):
            t = 0-sor[i]
            l = i+1
            r = len(sor) - 1
            while l<r:
                if sor[l]+sor[r] == t:
                    if [sor[i], sor[l], sor[r]] not in out:
                        out.append([sor[i], sor[l], sor[r]])
                if sor[l]+sor[r] > t:
                    r-=1
                else:
                    l+=1
        return out
        
