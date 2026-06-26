class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        max_vol = 0

        for i in range(n):
            h = min(height[left], height[right])
            w = right - left
            max_vol = max(max_vol, w * h)

            if height[left] > height[right]: right -= 1
            else: left += 1
        
        return max_vol
