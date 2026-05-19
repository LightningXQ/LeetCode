class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        visited_1 = set()
        visited_2 = set()

        iter1 = iter(nums1)
        iter2 = iter(nums2)

        a = next(iter1)
        b = next(iter2)

        while True:
            if a == b: return a
            else:
                visited_1.add(a)
                visited_2.add(b)

                if a > b:
                    try:
                        while b in visited_2: b = next(iter2)
                    except StopIteration:
                        return -1
                else:
                    try:
                        while a in visited_1: a = next(iter1)
                    except StopIteration:
                        return -1