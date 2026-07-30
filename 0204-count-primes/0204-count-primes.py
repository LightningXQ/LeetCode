class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0

        sieve = bytearray(b'\xff') * (n // 8 + 1)

        def get(i):
            return sieve[i >> 3] & (1 << (i & 7))

        def clear(i):
            sieve[i >> 3] &= ~(1 << (i & 7))

        clear(0)
        clear(1)

        for p in range(2, int(n ** 0.5) + 1):
            if get(p):
                for i in range(p * p, n, p):
                    clear(i)

        return sum(get(i) != 0 for i in range(n))
