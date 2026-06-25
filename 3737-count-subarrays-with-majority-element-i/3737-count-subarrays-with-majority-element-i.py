class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            sub_len = 0
            target_count = 0
            for j in range(i, n):
                sub_len += 1
                if nums[j] == target: target_count += 1
                if target_count * 2 > sub_len: count += 1
        return count
