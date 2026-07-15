class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        l_p = r_p = 0
        max_d = -1

        while l_p < m and r_p < n:
            if nums2[r_p] >= nums1[l_p]: 
                max_d += 1
                r_p += 1
            else:
                l_p += 1
                r_p += 1
        
        return max(max_d, 0)
