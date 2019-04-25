class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)

        # Length >= 2
        score = [1] * len(nums)
        minimum = [None, nums[0]]
        
        for i in range(1, len(nums)):
            for j in range(1, len(minimum)):
                if nums[i] > minimum[j] and j + 1 > score[i]:
                    score[i] = j + 1
                    if score[i] > len(minimum) - 1:
                        minimum.append(nums[i])
            if nums[i] < minimum[score[i]]:
                minimum[score[i]] = nums[i]
        return len(minimum) - 1
