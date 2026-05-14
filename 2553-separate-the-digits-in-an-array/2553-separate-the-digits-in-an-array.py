class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = list()

        for num in nums[::-1]:

            while num > 0:
                ans.append(num % 10)
                num //= 10

        return ans[::-1]
