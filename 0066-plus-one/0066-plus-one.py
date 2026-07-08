class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            d = digits[i]
            if d == 9: 
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
                    return digits
                digits[i] = 0
            else:
                digits[i] += 1
                return digits