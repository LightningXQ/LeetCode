class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = sum_even = 0

        for i in range(1, n * 2 + 1):
            if i % 2: sum_odd += i
            else: sum_even += i
        
        return math.gcd(sum_odd, sum_even)