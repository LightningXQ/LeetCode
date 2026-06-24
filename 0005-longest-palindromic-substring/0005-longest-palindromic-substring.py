class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        result = ""

        # odd-length palindrome
        for i in range(n):
            l = 1
            pivot_l = i - 1
            pivot_r = i + 1

            while pivot_l >= 0 and pivot_r <= n - 1 and s[pivot_l] == s[pivot_r]:
                l += 2
                pivot_l -= 1
                pivot_r += 1

            if l > max_len:
                result = s[pivot_l + 1:pivot_r]
                max_len = l

        # even-length palindrome
        for i in range(n - 1):
            l = 0
            pivot_l = i
            pivot_r = i + 1

            while pivot_l >= 0 and pivot_r <= n - 1 and s[pivot_l] == s[pivot_r]:
                l += 2
                pivot_l -= 1
                pivot_r += 1

            if l > max_len:
                result = s[pivot_l + 1:pivot_r]
                max_len = l

        return result

