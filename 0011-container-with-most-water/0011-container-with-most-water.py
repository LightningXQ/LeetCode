class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_height = max(height)
        h_map = [[] for _ in range(max_height + 1)]

        for i, h in enumerate(height):
            h_map[h].append(i)
        
        min_i, max_i = 10 ** 4 + 1, -1
        max_vol = 0

        for h, idxs in enumerate(h_map[::-1]):
            h = max_height - h
            if max_vol >= h * (n - 1): break 
            if not idxs: continue
            min_i, max_i = min(min(idxs), min_i), max(max(idxs), max_i)
            max_vol = max(max_vol, h * (max_i - min_i))
        
        return max_vol
