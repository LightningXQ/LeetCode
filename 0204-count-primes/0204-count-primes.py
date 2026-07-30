class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        if n == 3: return 1

        from math import isqrt
        seg_size = max(isqrt(n), 1)

        is_prime = [False, False] + [True] * (seg_size - 1)
        for p in range(2, isqrt(seg_size) + 1):
            if is_prime[p]:
                for i in range(p * p, seg_size + 1, p):
                    is_prime[i] = False
        small_primes = [p for p in range(2, seg_size + 1) if is_prime[p]]

        count = 0
        for low in range(0, n, seg_size):
            high = min(low + seg_size, n)
            size = high - low

            seg = bytearray(b'\xff') * (size // 8 + 1)

            if low == 0:
                seg[0] &= ~0b11  # clear bits 0 and 1

            for p in small_primes:
                start = max(p * p, ((low + p - 1) // p) * p) - low
                for j in range(start, size, p):
                    seg[j >> 3] &= ~(1 << (j & 7))

            for j in range(size):
                if seg[j >> 3] & (1 << (j & 7)):
                    count += 1

        return count
