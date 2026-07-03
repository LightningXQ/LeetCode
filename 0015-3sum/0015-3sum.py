class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = list()
        for i in range(n - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0: break
            if nums[i] + nums[n - 1] + nums[n - 2] < 0: continue

            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1; r -= 1
                else:
                    if total > 0: r -= 1
                    if total < 0: l += 1

        return result
