class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b, a, l, o, n = 0, 0, 0, 0, 0

        for c in text:
            match c:
                case 'b': b += 1
                case 'a': a += 1
                case 'l': l += 1
                case 'o': o += 1
                case 'n': n += 1

        return min(b, a, l // 2, o // 2, n)
