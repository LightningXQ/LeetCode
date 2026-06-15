class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_sum = [0]
        temp = 0
        for num in nums:
            temp += num
            prefix_sum.append(temp)

        total_sum = temp
        result = list()

        for i in range(n):
            result.append(abs(total_sum - prefix_sum[i + 1] - prefix_sum[i]))

        return result
