class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = dict()
        for idx, num in enumerate(nums):
            if num not in dic: dic[num] = [idx]
            else: dic[num].append(idx)

        result = [0] * n

        for vals in dic.values():
            total = sum(vals)
            m = len(vals)
            prefix_sum = 0
            
            for i, idx in enumerate(vals):
                result[idx] = total - prefix_sum * 2 + idx * (2 * i - m)
                prefix_sum += idx
        return result
