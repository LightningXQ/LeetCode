class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        if n < 9:       return n
        elif n < 17:    return 2 * n - 8    # n + (n - 8)
        elif n < 25:    return 3 * n - 24   # n + (n - 8) + (n - 16)
        else:           return 4 * n - 48   # n + (n - 8) + (n - 16) + (n - 24)