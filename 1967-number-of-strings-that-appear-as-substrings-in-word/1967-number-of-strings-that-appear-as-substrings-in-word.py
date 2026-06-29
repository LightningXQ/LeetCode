class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for p in patterns:
            if word.__contains__(p): result += 1

        return result