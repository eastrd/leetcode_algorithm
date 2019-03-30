class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search the number
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        # print(l, mid, r)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target > nums[mid] and target < nums[mid + 1]:
            return mid + 1
        return mid
