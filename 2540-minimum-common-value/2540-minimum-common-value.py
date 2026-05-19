class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        bias = nums1[-1]

        visited = set()

        iter1 = iter(nums1)
        iter2 = iter(nums2)

        a = next(iter1)
        b = next(iter2)

        while True:
            if a == b: return a
            else:
                visited.add(a)
                visited.add(b + bias)

                if a > b:
                    try:
                        while b + bias in visited: b = next(iter2)
                    except StopIteration:
                        return -1
                else:
                    try:
                        while a in visited: a = next(iter1)
                    except StopIteration:
                        return -1