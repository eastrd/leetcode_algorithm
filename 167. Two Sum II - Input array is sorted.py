class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # diff: index
        diff_dict = {}
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if numbers[i] in diff_dict and diff_dict[numbers[i]] != i:
                return sorted([i + 1, diff_dict[numbers[i]] + 1])
            diff_dict[diff] = i
            
            rev_i = len(numbers)-i-1
            
            diff2 = target - numbers[rev_i]
            if numbers[rev_i] in diff_dict and diff_dict[numbers[rev_i]] != rev_i:
                return sorted([len(numbers)-i, diff_dict[numbers[rev_i]] + 1])
            diff_dict[diff2] = rev_i
