class Solution:
    def processStr(self, s: str) -> str:
        result = list()

        for ch in s:
            match ch:
                case '*':
                    if len(result): result.pop()
                case '#':   result += result
                case '%':   result = result[::-1]
                case _:     result.append(ch)

        return ''.join(result)
