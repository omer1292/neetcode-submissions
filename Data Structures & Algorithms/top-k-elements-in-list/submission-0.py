class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] +=1
            else:
                hm[nums[i]] = 1
        return [x[0] for x in sorted(hm.items(), key=lambda x: x[1], reverse=True)[:k]]
        
        