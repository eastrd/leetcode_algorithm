class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        max = curr = 0
        pre = -1
        while i < len(nums):
            if nums[i] == 1:
                curr += 1
            else:
                # already set last_0
                pre = curr
                curr = 0
            if pre + curr + 1 > max:
                max = curr + pre + 1
            i += 1
        return max
