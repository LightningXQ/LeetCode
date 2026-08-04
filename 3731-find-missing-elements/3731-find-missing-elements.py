class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums: return list()
            
        l, h = min(nums), max(nums)
        bit_flags = 0

        for num in nums:
            bit_flags |= (1 << (num - l))
        
        result = []
        for i in range(h - l + 1):
            if not (bit_flags & (1 << i)):
                result.append(l + i)
        
        return result
