class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        ans = 0

        tasks.sort(key=lambda x: x[1] - x[0])

        for task in tasks:
            ans = max(ans + task[0], task[1])

        return ans
