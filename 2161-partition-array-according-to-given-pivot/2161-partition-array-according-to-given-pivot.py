class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left, mid, right = list(), list(), list()

        for num in nums:
            if num < pivot: left.append(num)
            elif num == pivot: mid.append(num)
            else: right.append(num)

        return left + mid + right
