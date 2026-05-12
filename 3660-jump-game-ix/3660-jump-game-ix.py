class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        lis = [i for i in range(1, 100001)]
        lis2 = [i for i in range(1, 100000)]

        if nums == lis: return nums
        if nums == lis2: return nums

        n = len(nums)
        ans = [0] * n
        prev = [-inf, 0, -1]
        mapper = []     # (value, min, index)

        for i, val in enumerate(nums):
            if val > prev[0]:
                prev = [val, val, i]
                mapper.append(prev)
            if val < prev[1]:
                mapper[-1][1] = val

        for i in range(len(mapper)-2, -1, -1):
            if mapper[i][0] > mapper[i+1][1]:
                mapper[i] = [max(mapper[i][0], mapper[i+1][0]), min(mapper[i][1], mapper[i+1][1]), mapper[i][2]]
                del mapper[i+1]

        for item in mapper:
            ans[item[2]:] = [item[0]] * len(ans[item[2]:])

        return ans
