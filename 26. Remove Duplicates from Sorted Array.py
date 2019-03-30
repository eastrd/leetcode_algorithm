class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        t = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[t]:
                t += 1
                nums[t] = nums[i]
        
        return t + 1
