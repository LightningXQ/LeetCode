class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        if not restrictions: return n - 1

        restrictions.append([1, 0])
        restrictions.sort(key=lambda a: a[0])

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        r_len = len(restrictions)
        max_height = 0

        for i in range(1, r_len):
            l_x, l_y, r_x, r_y = restrictions[i - 1] + restrictions[i]
            restrictions[i][1] = min(r_y, l_y + (r_x - l_x))

        for i in range(r_len - 2, -1, -1):
            l_x, l_y, r_x, r_y = restrictions[i] + restrictions[i + 1]
            restrictions[i][1] = min(l_y, r_y + (r_x - l_x))

        for i in range(r_len - 1):
            l_x, l_y, r_x, r_y = restrictions[i] + restrictions[i + 1]
            peak_height = (l_y + r_y + (r_x - l_x)) // 2
            max_height = max(max_height, peak_height)

        return max_height