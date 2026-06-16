class Solution:
    def processStr(self, s: str) -> str:
        result = list()

        for ch in s:
            if ch == '*':
                if len(result): result.pop()
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
            else: result.append(ch)

        return ''.join(result)
