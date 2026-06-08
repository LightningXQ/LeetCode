class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n = len(nums)
        n_left, n_mid, n_right = 0, 0, 0

        for num in nums:
            if num < pivot: n_left += 1
            elif num == pivot: n_mid += 1
            else: n_right += 1

        ans = [0] * n
        i_left, i_mid, i_right = 0, n_left, n_left + n_mid

        for num in nums:
            if num < pivot: ans[i_left] = num; i_left += 1
            elif num == pivot: ans[i_mid] = num; i_mid += 1
            else: ans[i_right] = num; i_right += 1

        return ans
