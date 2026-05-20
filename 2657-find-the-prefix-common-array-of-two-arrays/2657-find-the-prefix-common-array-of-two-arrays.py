class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        set_a = set()
        set_b = set()
        result = list()

        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            intersection = set_a & set_b
            result.append(len(intersection))

        return result
