class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min([len(s) for s in strs])
        if not l: return ""
        result = str()
        for i in range(l):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return result
            result += c
        return result