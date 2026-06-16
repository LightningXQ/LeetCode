class Solution:
    def processStr(self, s: str) -> str:
        result = list()

        for ch in s:
            if ch.islower(): result.append(ch)
            if ch == '*':
                if result: result.pop()
            if ch == '#':
                result += result
            if ch == '%':
                result.reverse()

        return ''.join(result)
