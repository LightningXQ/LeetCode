class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))

        if len(b) > len(a): a, b = b, a
        bias = len(a) - len(b)
        carry = 0
        result = ""

        for i in range(n - 1, -1, -1):
            a_i = i
            b_i = i - bias

            if b_i >= 0:
                a_v = int(a[a_i])
                b_v = int(b[b_i])
                total = a_v + b_v + carry

                result += str(total % 2)
                carry = total >= 2
            else:
                a_v = int(a[a_i])
                total = a_v + carry
                
                result += str(total % 2)
                carry = total >= 2

        if carry: result += str(int(carry)) 

        return result[::-1]