class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return len(sorted("".join([str(i) for i in nums]).split("0"), key=lambda x: -len(x))[0])
