class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)

        # Length >= 2
        seq = [0] * len(nums)
        seq[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and seq[j] + 1 > seq[i]:
                    seq[i] = seq[j] + 1
                if seq[i] == 0:
                    seq[i] = 1
        return max(seq)
