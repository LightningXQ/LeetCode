class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1 & set2

        return min(intersection) if len(intersection) else -1
