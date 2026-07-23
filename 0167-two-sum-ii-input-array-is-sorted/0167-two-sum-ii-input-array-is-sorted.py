class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, n - 1

        while True:
            lv, rv = numbers[l], numbers[r]
            lrvsum = lv + rv

            if lrvsum == target: return [l + 1, r + 1]
            if lrvsum < target: l += 1
            if lrvsum > target: r -= 1
