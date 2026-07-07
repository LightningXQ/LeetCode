class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = list()
        total = 0
        for num in str(n):
            if num != "0":
                nums.append(num)
                total += int(num)
        
        if not nums: return 0
        x = int("".join(nums))

        return x * total