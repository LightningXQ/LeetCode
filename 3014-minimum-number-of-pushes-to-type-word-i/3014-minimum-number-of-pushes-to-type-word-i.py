class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        # Approach 1

        if n < 9:       return n
        elif n < 17:    return 2 * n - 8    # n + (n - 8)
        elif n < 25:    return 3 * n - 24   # n + (n - 8) + (n - 16)
        else:           return 4 * n - 48   # n + (n - 8) + (n - 16) + (n - 24)

        # Approach 2

        # d = [
        #     None, 1, 2, 3, 4, 5, 6, 7, 8, 
        #     10, 12, 14, 16, 18, 20, 22, 24, 
        #     27, 30, 33, 36, 39, 42, 45, 48, 
        #     52, 56
        # ]

        # return d[n]
