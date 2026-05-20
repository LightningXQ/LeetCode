class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        m = n // 2

        # difference array
        # diff[i] = number of modifications required when the sum is i
        # i <= [0, 1, 2, ... , 2 * limit, 2 * limit + 1]
        diff = [0] * (2 * limit + 2)

        for i in range(m):
            a = min(nums[i], nums[n - i - 1])
            b = max(nums[i], nums[n - i - 1])

            diff[2] += 2
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1

        curr_moves = 0
        min_moves = n

        for i in diff[2:]:
            curr_moves = curr_moves + i
            if min_moves > curr_moves:
                min_moves = curr_moves

        return min_moves
