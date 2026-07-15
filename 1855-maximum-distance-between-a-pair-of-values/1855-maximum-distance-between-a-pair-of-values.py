class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        l_p = r_p = 0
        max_d = 0

        for i in range(m + n):
            if l_p >= m or r_p >= n: return max_d
            if nums2[r_p] >= nums1[l_p]: 
                max_d = max(max_d, r_p - l_p)
                r_p += 1
            else:
                l_p += 1
                r_p += 1
