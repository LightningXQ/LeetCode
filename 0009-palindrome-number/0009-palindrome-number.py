class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x.__str__()
        n = len(s)
        for i in range(n // 2):
            if not s[i] == s[n - i - 1]: break
        else: return True
        return False