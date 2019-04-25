class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        len1, len2 = len(nums1), len(nums2)
        if len1 + len2 == 0:
            return 0
        if len1 == len2 == 1:
            return (nums1[0] + nums2[0]) / 2
        
        i = j = 0
        while i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
            else:
                res.append(nums1[i])
                i += 1
        
        if i < len1:
            res.extend(nums1[i:])
        elif j < len2:
            res.extend(nums2[j:])

        if len(res) % 2 == 0:
            return (res[len(res)//2] + res[len(res)//2 - 1]) / 2
        return res[len(res) // 2]
