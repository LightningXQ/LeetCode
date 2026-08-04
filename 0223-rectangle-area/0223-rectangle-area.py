class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)

        if ax2 <= bx1 or bx2 <= ax1: return a + b
        if ay2 <= by1 or by2 <= ay1: return a + b

        if ax1 <= bx1:
            if ax2 <= bx2: x = ax2 - bx1
            else: x = bx2 - bx1
        else:
            if ax2 <= bx2: x = ax2 - ax1
            else: x = bx2 - ax1
        
        if ay1 <= by1:
            if ay2 <= by2: y = ay2 - by1
            else: y = by2 - by1
        else:
            if ay2 <= by2: y = ay2 - ay1
            else: y = by2 - ay1
        
        return a + b - x * y
