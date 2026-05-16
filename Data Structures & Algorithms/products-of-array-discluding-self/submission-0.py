from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = reduce(mul, nums)
        out = []
        zs = 0
        hm={}
        for i in range(len(nums)):
            if nums[i]==0:
                zs+=1
                hm[0] = i
        nums2 = []
        if zs == 1:
            for i in nums:
                if i!=0:
                    nums2.append(i)
            res2 = reduce(mul, nums2)
        for i in nums:
            if i!=0:
                out.append(int(res/i))
            if i == 0:
                if zs == 1:
                    out.append(int(res2))
                else:
                    out.append(0)
        return out