class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        m = n // 2

        diff = [0] * (2 * limit + 2)

        for i in range(m):
            a = min(nums[i], nums[n - i - 1])
            b = max(nums[i], nums[n - i - 1])

            diff[2] += 2
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1

        curr = 0
        result = list()

        for i in diff:
            curr = curr + i
            result.append(curr)

        return min(result[2:])






