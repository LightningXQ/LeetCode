class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums)

        ans_list = [i for i in range(1, n+1)]
        ans_list[-1] = n - 1

        nums.sort()
        ans = nums == ans_list

        return ans
