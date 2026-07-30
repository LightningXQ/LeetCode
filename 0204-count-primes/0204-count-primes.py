class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0

        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n, p):
                    # mark as false multiples of p
                    # p * 2, p * 3, ... , p * (p - 1) are already marked at i == 2, 3, ... , p - 1
                    sieve[i] = False
        return len([i for i, val in enumerate(sieve) if val])
