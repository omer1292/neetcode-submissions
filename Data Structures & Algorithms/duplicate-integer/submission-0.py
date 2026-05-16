class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm ={}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = i
            else:
                return True
        return False