class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        result = ""

        for i in range(n):
            # odd-length palindrome
            l_odd = 1
            pivot_l = i - 1
            pivot_r = i + 1

            while pivot_l >= 0 and pivot_r <= n - 1 and s[pivot_l] == s[pivot_r]:
                l_odd += 2
                pivot_l -= 1
                pivot_r += 1

            if l_odd > max_len:
                result = s[pivot_l + 1:pivot_r]
                max_len = l_odd

            if i == n - 1: break

            # even-length palindrome
            l_even = 0
            pivot_l = i
            pivot_r = i + 1

            while pivot_l >= 0 and pivot_r <= n - 1 and s[pivot_l] == s[pivot_r]:
                l_even += 2
                pivot_l -= 1
                pivot_r += 1

            if l_even > max_len:
                result = s[pivot_l + 1:pivot_r]
                max_len = l_even

        return result

