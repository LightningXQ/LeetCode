class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        if n < 9:       return n
        elif n < 17:    return n + (n - 8)
        elif n < 25:    return n + (n - 8) + (n - 16)
        else:           return n + (n - 8) + (n - 16) + (n - 24)