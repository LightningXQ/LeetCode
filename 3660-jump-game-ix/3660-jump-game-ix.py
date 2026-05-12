class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prev = [-inf, inf, -1]    # (max, min, index)
        prev_max = list()

        for i, val in enumerate(nums):
            if val > prev[0]:
                prev = [val, val, i]
                prev_max.append(prev)
            if val < prev[1]:
                prev_max[-1][1] = val

        for i in range(len(prev_max)-2, -1, -1):
            if prev_max[i][0] > prev_max[i+1][1]:
                prev_max[i][0] = prev_max[i+1][0]
                prev_max[i][1] = min(prev_max[i][1], prev_max[i+1][1])

        for i in range(len(prev_max)):
            if not prev_max[i] == prev_max[-1]:
                start = prev_max[i][2]
                end = prev_max[i+1][2]
                ans[start:end] = [prev_max[i][0]] * (end - start)
            else:
                start = prev_max[i][2]
                end = n
                ans[start:end] = [prev_max[i][0]] * (end - start)

        return ans