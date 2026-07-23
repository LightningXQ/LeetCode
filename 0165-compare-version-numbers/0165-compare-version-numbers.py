class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        m, n = len(v1), len(v2)

        for i in range(max(m, n)):
            v1_v = int(v1[i]) if i < m else 0
            v2_v = int(v2[i]) if i < n else 0
            
            if v1_v > v2_v: return 1
            if v1_v < v2_v: return -1

        return 0
