class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        common_set = set()
        prefix = 0
        result = list()

        for i in range(n):
            a, b = A[i], B[i]

            if a in common_set: prefix += 1
            else: common_set.add(a)

            if b in common_set: prefix += 1
            else: common_set.add(b)

            result.append(prefix)

        return result
