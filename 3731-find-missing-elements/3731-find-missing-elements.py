class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, h = 101, 0
        elms = bytearray(101)

        for num in nums:
            if num > h: h = num
            if num < l: l = num
            elms[num] = 1
        
        result = list()
        for i in range(l, h + 1):
            if not elms[i]: result.append(i)
        
        return result   
