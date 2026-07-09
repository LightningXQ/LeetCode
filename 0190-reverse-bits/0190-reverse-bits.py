class Solution:
    def reverseBits(self, n: int) -> int:
        q, r = n, 0
        string = ""

        while q > 0:
            string += str(q % 2)
            q //= 2
        
        n = len(string)
        string += ("0" * (32 - n))

        return int(string, 2)
