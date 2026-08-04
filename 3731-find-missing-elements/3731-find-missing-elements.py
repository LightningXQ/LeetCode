class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, h = 101, 0
        elms = [False] * 101

        for num in nums:
            if num > h: h = num
            if num < l: l = num
            elms[num] = True
        
        result = list()
        for i in range(l, h + 1):
            if not elms[i]: result.append(i)
        
        return result   
