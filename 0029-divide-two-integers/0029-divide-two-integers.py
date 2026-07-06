class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        if divisor == 1:
            return dividend

        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            d = divisor

            amplifier = 1
            while dividend >= d * 2: 
                d *= 2 
                amplifier *= 2

            dividend -= d
            result += amplifier
        
        result *= sign

        minimum = -1 * (2 ** 31)
        maximum = 2 ** 31 - 1
        result = minimum if result < minimum else result
        result = maximum if result > maximum else result

        return result