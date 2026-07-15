class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = sum(matrix, list())

        idx = bisect.bisect_left(flatten, target)
        return idx < len(flatten) and flatten[idx] == target