class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1, -1, -1]
        result = 0

        for i, c in enumerate(s):
            if c == "a": pos[0] = i
            if c == "b": pos[1] = i
            if c == "c": pos[2] = i
            result += min(pos) + 1
        
        return result
        