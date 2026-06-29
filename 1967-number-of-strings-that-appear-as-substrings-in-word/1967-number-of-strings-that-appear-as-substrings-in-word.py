class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        len_w = len(word)
        result = 0
        for p in patterns:
            n = len(p)
            if n > len_w: continue
            for i in range(len_w - n + 1):
                if word[i:i + n] == p: 
                    result += 1
                    break

        return result